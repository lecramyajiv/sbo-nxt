#define QT_CLEAN_NAMESPACE
#include "qtkdeintegration_x11_p.h"

#include <qcolordialog.h>
#include <qfiledialog.h>
#include <qfontdialog.h>
#include <qlibrary.h>
#include <qregexp.h>
#include <qmessagebox.h>
#include <stdlib.h>

bool QKDEIntegration::inited = false;
bool QKDEIntegration::enable = false;

bool QKDEIntegration::enabled()
    {
    if( !inited )
        initLibrary();
    return enable;
    }

static QCString findLibrary()
    {
    if( getenv( "QT_NO_KDE_INTEGRATION" ) == NULL
        || getenv( "QT_NO_KDE_INTEGRATION" )[ 0 ] == '0' )
        {
#ifdef USE_LIB64_PATHES
        return "/opt/kde3/lib64/kde3/plugins/integration/libqtkde";
#else
        return "/opt/kde3/lib/kde3/plugins/integration/libqtkde";
#endif
        }
    return "";
    }

inline static long widgetToWinId( const QWidget* w )
    {
    return w != NULL ? w->winId() : 0;
    }

inline static QFont fontPtrToFontRef( const QFont* f )
    {
    return f != NULL ? *f : QFont();
    }

// ---
static bool (*qtkde_initializeIntegration)( );
static QStringList (*qtkde_getOpenFileNames)( const QString& filter, QString* workingDirectory,
    long parent, const QCString& name, const QString& caption, QString* selectedFilter,
    bool multiple );
static QString (*qtkde_getSaveFileName)( const QString& initialSelection, const QString& filter,
    QString* workingDirectory, long parent, const QCString& name, const QString& caption,
    QString* selectedFilter );
static QString (*qtkde_getExistingDirectory)( const QString& initialDirectory, long parent,
    const QCString& name, const QString& caption );
static QColor (*qtkde_getColor)( const QColor& color, long parent, const QCString& name );
static QFont (*qtkde_getFont)( bool* ok, const QFont& def, long parent, const QCString& name );
static int (*qtkde_messageBox1)( int type, long parent, const QString& caption, const QString& text,
    int button0, int button1, int button2 );
static int (*qtkde_messageBox2)( int type, long parent, const QString& caption, const QString& text,
    const QString& button0Text, const QString& button1Text, const QString& button2Text,
    int defaultButton, int escapeButton );

void QKDEIntegration::initLibrary()
    {
    if( !inited )
        {
        enable = false;
        inited = true;
        QString libpath = findLibrary();
        if( libpath.isEmpty())
            return;
        QLibrary lib( libpath );
        lib.setAutoUnload( false );
        qtkde_initializeIntegration = (
            bool (*)( )
            )
            lib.resolve("initializeIntegration");
        if( qtkde_initializeIntegration == NULL )
            return;
        qtkde_getOpenFileNames = (
            QStringList (*)( const QString& filter, QString* workingDirectory, long parent,
                const QCString& name, const QString& caption, QString* selectedFilter,
                bool multiple )
            )
            lib.resolve("getOpenFileNames");
        if( qtkde_getOpenFileNames == NULL )
            return;
        qtkde_getSaveFileName = (
            QString (*)( const QString& initialSelection, const QString& filter, QString* workingDirectory,
                long parent, const QCString& name, const QString& caption, QString* selectedFilter )
            )
            lib.resolve("getSaveFileName");
        if( qtkde_getSaveFileName == NULL )
            return;
        qtkde_getExistingDirectory = (
            QString (*)( const QString& initialDirectory, long parent, const QCString& name,
                const QString& caption )
            )
            lib.resolve("getExistingDirectory");
        if( qtkde_getExistingDirectory == NULL )
            return;
        qtkde_getColor = (
            QColor (*)( const QColor& color, long parent, const QCString& name )
            )
            lib.resolve("getColor");
        if( qtkde_getColor == NULL )
            return;
        qtkde_getFont = (
            QFont (*)( bool* ok, const QFont& def, long parent, const QCString& name )
            )
            lib.resolve("getFont");
        if( qtkde_getFont == NULL )
            return;
        qtkde_messageBox1 = (
            int (*)( int type, long parent, const QString& caption, const QString& text,
                int button0, int button1, int button2 )
            )
            lib.resolve("messageBox1");
        if( qtkde_messageBox1 == NULL )
            return;
        qtkde_messageBox2 = (
            int (*)( int type, long parent, const QString& caption, const QString& text,
                const QString& button0Text, const QString& button1Text, const QString& button2Text,
                int defaultButton, int escapeButton )
            )
            lib.resolve("messageBox2");
        if( qtkde_messageBox2 == NULL )
            return;
        enable = qtkde_initializeIntegration();
        }
    }

bool QKDEIntegration::initializeIntegration( )
    {
    return qtkde_initializeIntegration(
         );
    }
QStringList QKDEIntegration::getOpenFileNames( const QString& filter, QString* workingDirectory,
    QWidget* parent, const char* name, const QString& caption, QString* selectedFilter,
    bool multiple )
    {
    return qtkde_getOpenFileNames(
        filter, workingDirectory, widgetToWinId( parent ), name, caption, selectedFilter, multiple );
    }
QString QKDEIntegration::getSaveFileName( const QString& initialSelection, const QString& filter,
    QString* workingDirectory, QWidget* parent, const char* name, const QString& caption,
    QString* selectedFilter )
    {
    return qtkde_getSaveFileName(
        initialSelection, filter, workingDirectory, widgetToWinId( parent ), name, caption, selectedFilter );
    }
QString QKDEIntegration::getExistingDirectory( const QString& initialDirectory, QWidget* parent,
    const char* name, const QString& caption )
    {
    return qtkde_getExistingDirectory(
        initialDirectory, widgetToWinId( parent ), name, caption );
    }
QColor QKDEIntegration::getColor( const QColor& color, QWidget* parent, const char* name )
    {
    return qtkde_getColor(
        color, widgetToWinId( parent ), name );
    }
QFont QKDEIntegration::getFont( bool* ok, const QFont* def, QWidget* parent, const char* name )
    {
    return qtkde_getFont(
        ok, fontPtrToFontRef( def ), widgetToWinId( parent ), name );
    }
int QKDEIntegration::messageBox1( int type, QWidget* parent, const QString& caption,
    const QString& text, int button0, int button1, int button2 )
    {
    return qtkde_messageBox1(
        type, widgetToWinId( parent ), caption, text, button0, button1, button2 );
    }
int QKDEIntegration::messageBox2( int type, QWidget* parent, const QString& caption,
    const QString& text, const QString& button0Text, const QString& button1Text, const QString& button2Text,
    int defaultButton, int escapeButton )
    {
    return qtkde_messageBox2(
        type, widgetToWinId( parent ), caption, text, button0Text, button1Text, button2Text, defaultButton, escapeButton );
    }
// ---

int QKDEIntegration::information( QWidget* parent, const QString& caption,
    const QString& text, int button0, int button1, int button2 )
    {
    return qtkde_messageBox1(
        QMessageBox::Information, widgetToWinId( parent ), caption, text, button0, button1, button2 );
    }

int QKDEIntegration::question( QWidget* parent, const QString& caption,
    const QString& text, int button0, int button1, int button2 )
    {
    return qtkde_messageBox1(
        QMessageBox::Question, widgetToWinId( parent ), caption, text, button0, button1, button2 );
    }

int QKDEIntegration::warning( QWidget* parent, const QString& caption,
    const QString& text, int button0, int button1, int button2 )
    {
    return qtkde_messageBox1(
        QMessageBox::Warning, widgetToWinId( parent ), caption, text, button0, button1, button2 );
    }

int QKDEIntegration::critical( QWidget* parent, const QString& caption,
    const QString& text, int button0, int button1, int button2 )
    {
    return qtkde_messageBox1(
        QMessageBox::Critical, widgetToWinId( parent ), caption, text, button0, button1, button2 );
    }

int QKDEIntegration::information( QWidget* parent, const QString& caption,
    const QString& text, const QString& button0Text, const QString& button1Text, const QString& button2Text,
    int defaultButton, int escapeButton )
    {
    return qtkde_messageBox2(
        QMessageBox::Information, widgetToWinId( parent ), caption, text, button0Text, button1Text, button2Text, defaultButton, escapeButton );
    }

int QKDEIntegration::question( QWidget* parent, const QString& caption,
    const QString& text, const QString& button0Text, const QString& button1Text, const QString& button2Text,
    int defaultButton, int escapeButton )
    {
    return qtkde_messageBox2(
        QMessageBox::Question, widgetToWinId( parent ), caption, text, button0Text, button1Text, button2Text, defaultButton, escapeButton );
    }

int QKDEIntegration::warning( QWidget* parent, const QString& caption,
    const QString& text, const QString& button0Text, const QString& button1Text, const QString& button2Text,
    int defaultButton, int escapeButton )
    {
    return qtkde_messageBox2(
        QMessageBox::Warning, widgetToWinId( parent ), caption, text, button0Text, button1Text, button2Text, defaultButton, escapeButton );
    }

int QKDEIntegration::critical( QWidget* parent, const QString& caption,
    const QString& text, const QString& button0Text, const QString& button1Text, const QString& button2Text,
    int defaultButton, int escapeButton )
    {
    return qtkde_messageBox2(
        QMessageBox::Critical, widgetToWinId( parent ), caption, text, button0Text, button1Text, button2Text, defaultButton, escapeButton );
    }
