#ifndef QKDEINTEGRATION_H
#define QKDEINTEGRATION_H

#include <qstringlist.h>

class QLibrary;
class QWidget;
class QColor;
class QFont;

class QKDEIntegration
    {
    public:
        static bool enabled();
// --- 
        static bool initializeIntegration( );
        static QStringList getOpenFileNames( const QString& filter, QString* workingDirectory,
            QWidget* parent, const char* name, const QString& caption, QString* selectedFilter,
            bool multiple );
        static QString getSaveFileName( const QString& initialSelection, const QString& filter,
            QString* workingDirectory, QWidget* parent, const char* name, const QString& caption,
            QString* selectedFilter );
        static QString getExistingDirectory( const QString& initialDirectory, QWidget* parent,
            const char* name, const QString& caption );
        static QColor getColor( const QColor& color, QWidget* parent, const char* name );
        static QFont getFont( bool* ok, const QFont* def, QWidget* parent, const char* name );
        static int messageBox1( int type, QWidget* parent, const QString& caption,
            const QString& text, int button0, int button1, int button2 );
        static int information( QWidget* parent, const QString& caption, const QString& text,
            int button0, int button1, int button2 );
        static int question( QWidget* parent, const QString& caption, const QString& text,
            int button0, int button1, int button2 );
        static int warning( QWidget* parent, const QString& caption, const QString& text,
            int button0, int button1, int button2 );
        static int critical( QWidget* parent, const QString& caption, const QString& text,
            int button0, int button1, int button2 );
        static int messageBox2( int type, QWidget* parent, const QString& caption,
            const QString& text, const QString& button0Text, const QString& button1Text,
            const QString& button2Text, int defaultButton, int escapeButton );
        static int information( QWidget* parent, const QString& caption, const QString& text,
            const QString& button0Text, const QString& button1Text, const QString& button2Text,
            int defaultButton, int escapeButton );
        static int question( QWidget* parent, const QString& caption, const QString& text,
            const QString& button0Text, const QString& button1Text, const QString& button2Text,
            int defaultButton, int escapeButton );
        static int warning( QWidget* parent, const QString& caption, const QString& text,
            const QString& button0Text, const QString& button1Text, const QString& button2Text,
            int defaultButton, int escapeButton );
        static int critical( QWidget* parent, const QString& caption, const QString& text,
            const QString& button0Text, const QString& button1Text, const QString& button2Text,
            int defaultButton, int escapeButton );
// ---
    private:
        static void initLibrary();
        static bool inited;
        static bool enable;
    };

#endif
