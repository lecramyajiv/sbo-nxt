Index: khelpcenter/navigator.cpp
===================================================================
--- khelpcenter/navigator.cpp.orig
+++ khelpcenter/navigator.cpp
@@ -121,8 +121,6 @@ Navigator::Navigator( View *view, QWidge
 
     mTabWidget = new QTabWidget( this );
     topLayout->addWidget( mTabWidget );
-    connect( mTabWidget, SIGNAL( currentChanged( QWidget * ) ),
-             SLOT( slotTabChanged( QWidget * ) ) );
 
     setupContentsTab();
     setupGlossaryTab();
@@ -136,6 +134,9 @@ Navigator::Navigator( View *view, QWidge
       mSearchWidget->updateScopeList();
       mSearchWidget->readConfig( KGlobal::config() );
     }
+
+    connect( mTabWidget, SIGNAL( currentChanged( QWidget * ) ),
+             SLOT( slotTabChanged( QWidget * ) ) );
 }
 
 Navigator::~Navigator()
