#
# spec file for package tdegames (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.2
%endif
%define tde_pkg tdegames
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:			trinity-%{tde_pkg}
Summary:		Trinity Desktop Environment - Games
Version:		%{tde_version}
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:		%{name}-rpmlintrc

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdemultimedia-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	fdupes
BuildRequires:	libtool

# AVAHI support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_avahi 1
BuildRequires:	libavahi-tqt-devel >= 1:0.6.30
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}avahi-client-devel
Requires:		%{_lib}avahi-client3
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	avahi-devel
Requires:		avahi
%endif
%endif

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if ( 0%{?rhel} && 0%{?rhel} <= 8 ) || ( 0%{?fedora} && 0%{?fedora} <= 33 ) || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# OPENSSL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}openssl-devel
%else
BuildRequires:	openssl-devel
%endif

# ACL support
%if 0%{?mdkver}
BuildRequires:	%{_lib}acl-devel
%else
BuildRequires:	libacl-devel
%endif

# ATTR support
%if 0%{?mgaversion} || 0%{?mdkversion}
%define libattr_devel %{_lib}attr-devel
%else
%define libattr_devel libattr-devel
%endif
BuildRequires: %{libattr_devel}

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# GLIB2 support
BuildRequires:	glib2-devel

Obsoletes:		trinity-kdegames < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdegames = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdegames-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdegames-libs = %{?epoch:%{epoch}:}%{version}-%{release}

Requires: trinity-libtdegames1 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdegames-card-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-atlantik = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kasteroids = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-katomic = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kbackgammon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kbattleship = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kblackbox = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kbounce = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kenolaba = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kfouleggs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kgoldrunner = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kjumpingcube = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klickety = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klines = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmahjongg = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmines = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-knetwalk = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kolf = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-konquest = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpat = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpoker = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kreversi = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksame = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kshisen = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksirtet = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksmiletris = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksnake = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksokoban = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kspaceduel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktron = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktuberling = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-twin4 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-lskat = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdefifteen = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Games and gaming libraries for the Trinity Desktop Environment.
Included with this package are: kenolaba, kasteroids, kblackbox, kmahjongg,
kmines, konquest, kpat, kpoker, kreversi, ksame, kshisen, ksmiletris,
ksnake, ksirtet, katomic, kjumpingcube, ktuberling.

%files

##########

%package devel
Summary:	Development files for %{name} 
Group:		Amusements/Games/Other

Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdelibs-devel >= %{tde_version}
Requires:	trinity-libtdegames-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-atlantik-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kolf-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-kdegames-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdegames-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Install %{name}-devel if you wish to develop or compile games for the
TDE desktop.

%files devel
%defattr(-,root,root,-)
%{tde_datadir}/cmake/libtdegames.cmake
%{tde_libdir}/pkgconfig/libtdegames.pc

##########

%package -n trinity-libtdegames1
Summary:	Trinity games library and common files
Group:		Amusements/Games/Other

%description -n trinity-libtdegames1
This library provides a common infrastructure for several of the
games in the TDE distribution. Features include standardized menu
items, high score handling, card display, and network connections
including chat capabilities.

This package is part of TDE, and a component of the TDE games module.

%files -n trinity-libtdegames1
%defattr(-,root,root,-)
%{tde_libdir}/libtdegames.so.*
%dir %{tde_datadir}/apps/tdegames
%dir %{tde_datadir}/apps/tdegames/pics
%{tde_datadir}/apps/tdegames/pics/star.png
%{tde_datadir}/icons/crystalsvg/*/actions/roll.png
%{tde_datadir}/icons/crystalsvg/*/actions/highscore.png

##########

%package -n trinity-libtdegames-devel
Summary:	Trinity games library headers
Group:		Development/Libraries/Other
Requires:	trinity-libtdegames1 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtdegames-devel
This package is necessary if you want to develop your own games using
the TDE games library.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-libtdegames-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_tdeincludedir}/kgame
%{tde_libdir}/libtdegames.so
%{tde_libdir}/libtdegames.la

##########

%package card-data
Summary:	Card decks for Trinity games
Group:		Amusements/Games/Other

%description card-data
Several different collections of card images for use by TDE games.

This package is part of Trinity, and a component of the TDE games module.

%files card-data
%defattr(-,root,root,-)
%{tde_datadir}/apps/carddecks/

##########

%package -n trinity-atlantik
Summary:	TDE client for Monopoly-like network games
Group:		Amusements/Games/Board/Other

%description -n trinity-atlantik
This is a TDE client for playing Monopoly-like boardgames on the
monopd network.  It can play any board supported by the network
server, including the classic Monopoly game, as well as the Atlantik
game in which the property includes several major cities in North
America and Europe.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-atlantik
%defattr(-,root,root,-)
%{tde_bindir}/atlantik
%{tde_libdir}/libatlantic.so.*
%{tde_libdir}/libatlantikclient.so.*
%{tde_libdir}/libatlantikui.so.*
%{tde_tdelibdir}/tdeio_atlantik.la
%{tde_tdelibdir}/tdeio_atlantik.so
%{tde_datadir}/services/atlantik.protocol
%{tde_tdeappdir}/atlantik.desktop
%{tde_datadir}/icons/hicolor/*/apps/atlantik.png
%{tde_datadir}/apps/atlantik/
%{tde_tdedocdir}/HTML/en/atlantik/
%{tde_mandir}/man*/atlantik.*

##########

%package -n trinity-atlantik-devel
Summary:	Development files for Atlantik
Group:		Development/Libraries/Other
Requires:	trinity-atlantik = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-atlantik-devel
This package contains header files for compiling programs against the
libraries which come with Atlantik.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-atlantik-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/atlantik
%{tde_tdeincludedir}/atlantic
%{tde_libdir}/libatlantic.so
%{tde_libdir}/libatlantic.la
%{tde_libdir}/libatlantikclient.so
%{tde_libdir}/libatlantikclient.la
%{tde_libdir}/libatlantikui.so
%{tde_libdir}/libatlantikui.la

##########

%package -n trinity-kasteroids
Summary:	Asteroids for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kasteroids
You know this game.  It is based on Warwick Allison's QwSpriteField
widget.

The objective of kasteroids is to destroy all the asteroids on the
screen to advance to the next level. Your ship is destroyed if it
makes contact with an asteroid.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kasteroids
%defattr(-,root,root,-)
%{tde_bindir}/kasteroids
%{tde_datadir}/icons/hicolor/*/apps/kasteroids.png
%{tde_tdeappdir}/kasteroids.desktop
%{tde_datadir}/apps/kasteroids/
%{tde_datadir}/config.kcfg/kasteroids.kcfg
%{tde_tdedocdir}/HTML/en/kasteroids/
%{tde_mandir}/man*/kasteroids.*

##########

%package -n trinity-katomic
Summary:	Atomic Entertainment game for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-katomic
This is a puzzle game, in which the object is to assemble a molecule
from its atoms on a Sokoban-like board.  On each move, an atom goes
as far as it can in a specified direction before being stopped by a
wall or another atom.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-katomic
%defattr(-,root,root,-)
%{tde_datadir}/apps/katomic/
%{tde_datadir}/icons/hicolor/*/apps/katomic.png
%{tde_tdeappdir}/katomic.desktop
%{tde_bindir}/katomic
%{tde_tdedocdir}/HTML/en/katomic/
%{tde_mandir}/man*/katomic.*

##########

%package -n trinity-kbackgammon
Summary:	A Backgammon game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kbackgammon
KBackgammon is a backgammon program for Trinity. It is based on the
code, ideas and concepts of KFibs (which is a FIBS client for
TDE1). For a short time, KBackgammon was called bacKgammon (if you
know somebody who is still using bacKgammon, please force them to
upgrade :-)).

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kbackgammon
%defattr(-,root,root,-)
%{tde_bindir}/kbackgammon
%{tde_tdeappdir}/kbackgammon.desktop
%{tde_datadir}/apps/kbackgammon/
%{tde_datadir}/icons/hicolor/*/apps/kbackgammon.png
%{tde_datadir}/icons/hicolor/*/apps/kbackgammon_engine.png
%{tde_tdedocdir}/HTML/en/kbackgammon/
%{tde_mandir}/man*/kbackgammon.*

##########

%package -n trinity-kbattleship
Summary:	Battleship game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kbattleship
This is an implementation of the Battleship game.  Each player tries
to be the first to sink all the opponent's ships by firing "blindly"
at them.  The game has options to play over a network connection or
against the computer.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kbattleship
%defattr(-,root,root,-)
%{tde_datadir}/apps/kbattleship/
%{tde_datadir}/apps/zeroconf/_kbattleship._tcp
%{tde_datadir}/icons/hicolor/*/apps/kbattleship.png
%{tde_tdeappdir}/kbattleship.desktop
%{tde_bindir}/kbattleship
%{tde_tdedocdir}/HTML/en/kbattleship/
%{tde_mandir}/man*/kbattleship.*

##########

%package -n trinity-kblackbox
Summary:	A simple logical game for the Trinity project
Group:		Amusements/Games/Board/Other

%description -n trinity-kblackbox
KBlackBox is a game of hide and seek played on an grid of boxes. Your
opponent (Random number generator, in this case) has hidden several
balls within this box. By shooting rays into the box and observing
where they emerge it is possible to deduce the positions of the
hidden balls. The fewer rays you use to find the balls, the lower
your score.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kblackbox
%defattr(-,root,root,-)
%{tde_datadir}/apps/kblackbox/
%{tde_datadir}/icons/hicolor/*/apps/kblackbox.png
%{tde_tdeappdir}/kblackbox.desktop
%{tde_bindir}/kblackbox
%{tde_tdedocdir}/HTML/en/kblackbox/
%{tde_mandir}/man*/kblackbox.*

##########

%package -n trinity-kbounce
Summary:	Jezzball clone for the K Desktop Environment
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kbounce
This is a clone of the popular Jezzball game originally created by
Microsoft. Jezzball is one of the rare and simple games requiring
skill, timing, and patience in order to be successful.  A ball begins
to bounce off of an area enclosed by four borders (like a
square). You must move your pointer to certain areas within the
square. Upon clicking, a new border is constructed at a relatively
quick pace. You can change the direction of the borders by 90 degrees
as well. Ultimately, you must force the ball to bounce around in a
smaller, and smaller area as time goes by without the ball ever
touching the borders as they are being constructed. If a ball touches
a certain part of the border as it is being built, the game is over.
After 75% of the original space has been blocked off from the moving
ball, you advance one level, and one more ball is added to the mix in
the following level.

This game was previously known as kjezz.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kbounce
%defattr(-,root,root,-)
%{tde_datadir}/apps/kbounce/
%{tde_tdeappdir}/kbounce.desktop
%{tde_datadir}/icons/hicolor/*/apps/kbounce.png
%{tde_bindir}/kbounce
%{tde_tdedocdir}/HTML/en/kbounce/
%{tde_mandir}/man*/kbounce.*

##########

%package -n trinity-kenolaba
Summary:	Enolaba board game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kenolaba
kenolaba is a simple board strategy game that is played by two
players. There are red and yellow pieces for each player. Beginning
from a start position where each player has 14 pieces, moves are
drawn until one player has pushed 6 pieces of his opponent out of the
board.

This game was previously known as kabalone, and was inspired by the
board game Abalone by Abalone SA, France.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kenolaba
%defattr(-,root,root,-)
%{tde_datadir}/apps/kenolaba/
%{tde_datadir}/icons/hicolor/*/apps/kenolaba.png
%{tde_tdeappdir}/kenolaba.desktop
%{tde_bindir}/kenolaba
%{tde_tdedocdir}/HTML/en/kenolaba/
%{tde_mandir}/man*/kenolaba.*

##########

%package -n trinity-kfouleggs
Summary:	A TDE clone of the Japanese PuyoPuyo game
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kfouleggs
KFouleggs is a clone of the Japanese PuyoPuyo game, with advanced
features such as multiplayer games against human or AI, and network
play.  If you have played Tetris or one of its many clones, you will
find KFouleggs easy to learn.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kfouleggs
%defattr(-,root,root,-)
%{tde_tdeappdir}/kfouleggs.desktop
%{tde_datadir}/apps/kfouleggs/
%{tde_datadir}/config.kcfg/kfouleggs.kcfg
%{tde_bindir}/kfouleggs
%{tde_datadir}/icons/hicolor/*/apps/kfouleggs.png
%{tde_tdedocdir}/HTML/en/kfouleggs/
%{tde_mandir}/man*/kfouleggs.*

##########

%package -n trinity-kgoldrunner
Summary:	A Trinity clone of the Loderunner arcade game
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kgoldrunner
KGoldrunner, a game of action and puzzle solving.  Run through the
maze, dodge your enemies, collect all the gold and climb up to the
next level.

You must guide the hero with the mouse or keyboard and collect all
the gold nuggets, then you can climb up into the next level.  Your
enemies are also after the gold and they will kill you if they catch
you!

The problem is you have no weapon to kill them.  All you can do is
run away, dig holes in the floor to trap them or lure them into some
area where they cannot hurt you.  After a short time a trapped enemy
climbs out of his hole, but if it closes before that, he will die and
reappear somewhere else.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kgoldrunner
%defattr(-,root,root,-)
%{tde_datadir}/apps/kgoldrunner/
%{tde_datadir}/icons/hicolor/*/apps/kgoldrunner.png
%{tde_tdeappdir}/KGoldrunner.desktop
%{tde_bindir}/kgoldrunner
%{tde_tdedocdir}/HTML/en/kgoldrunner/
%{tde_mandir}/man*/kgoldrunner.*

##########

%package -n trinity-kjumpingcube
Summary:	Tactical one or two player game
Group:		Amusements/Games/Strategy/Other

%description -n trinity-kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against a friend. The playing field consists of squares
that contains points.  By clicking on the squares you can increase
the points and if the points reach a maximum the points will jump to
the squares neighbours and take them over. Winner is the one, who
owns all squares.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kjumpingcube
%defattr(-,root,root,-)
%{tde_bindir}/kjumpingcube
%{tde_datadir}/icons/hicolor/*/apps/kjumpingcube.png
%{tde_datadir}/apps/kjumpingcube/
%{tde_tdeappdir}/kjumpingcube.desktop
%{tde_datadir}/config.kcfg/kjumpingcube.kcfg
%{tde_tdedocdir}/HTML/en/kjumpingcube/
%{tde_mandir}/man*/kjumpingcube.*

##########

%package -n trinity-klickety
Summary:	A Clickomania-like game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-klickety
Klickety is an adaptation of the (perhaps) well-known Clickomania
game; it is very similar to the "same" game.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-klickety
%defattr(-,root,root,-)
%{tde_bindir}/klickety
%{tde_tdeappdir}/klickety.desktop
%{tde_datadir}/icons/hicolor/*/apps/klickety.png
%{tde_datadir}/icons/crystalsvg/*/actions/endturn.png
%{tde_datadir}/apps/klickety/
%{tde_tdedocdir}/HTML/en/klickety/
%{tde_mandir}/man*/klickety.*

##########

%package -n trinity-klines
Summary:	Color lines for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-klines
KLines is a simple game. It is played by one player, so there is only
one winner :-). You play for fun and against the high score. It was
inspired by a well known game - "Color lines", written for DOS by
Olga Demina, Igor Demina, Igor Ivkin and Gennady Denisov back in
1992.

The main rules of the game are as simple as possible: you move (using
the mouse) marbles from cell to cell and build lines (horizontal,
vertical or diagonal). When a line contains 5 or more marbles, they
are removed and your score grows. After each turn the computer drops
three more marbles.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-klines
%defattr(-,root,root,-)
%{tde_datadir}/apps/klines/
%{tde_tdeappdir}/klines.desktop
%{tde_bindir}/klines
%{tde_datadir}/config.kcfg/klines.kcfg
%{tde_datadir}/icons/hicolor/*/apps/klines.png
%{tde_tdedocdir}/HTML/en/klines/
%{tde_mandir}/man*/klines.*

##########

%package -n trinity-kmahjongg
Summary:	The classic mahjongg game for Trinity project
Group:		Amusements/Games/Board/Other

%description -n trinity-kmahjongg
Your mission in this game is to remove all tiles from the game board. A
matching pair of tiles can be removed, if they are 'free', which means that
no other tiles block them on the left or right side.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kmahjongg
%defattr(-,root,root,-)
%{tde_datadir}/apps/kmahjongg/
%{tde_datadir}/icons/hicolor/*/apps/kmahjongg.png
%{tde_tdeappdir}/kmahjongg.desktop
%{tde_bindir}/kmahjongg
%{tde_datadir}/config.kcfg/kmahjongg.kcfg
%{tde_tdedocdir}/HTML/en/kmahjongg/
%{tde_mandir}/man*/kmahjongg.*

##########

%package -n trinity-kmines
Summary:	Minesweeper for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kmines
KMines is the classic Minesweeper game. You must uncover all the
empty cases without blowing on a mine.

When you uncover a case, a number appears : it indicates how many
mines surround this case. If there is no number the neighbour cases
are automatically uncovered. In your process of uncovering secure
cases, it is very useful to put a flag on the cases which contain a
mine.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kmines
%defattr(-,root,root,-)
%{tde_datadir}/icons/hicolor/*/apps/kmines.png
%{tde_tdeappdir}/kmines.desktop
%{tde_datadir}/apps/kmines/
%{tde_bindir}/kmines
%{tde_tdedocdir}/HTML/en/kmines/
%{tde_mandir}/man*/kmines.*

##########

%package -n trinity-knetwalk
Summary:	A game for system administrators
Group:		Amusements/Games/Board/Other

%description -n trinity-knetwalk
This game presents the player with a rectangular field consisting of
a server, several clients, and pieces of wire.  The object is to
rotate these elements until every client is connected to the server,
and no wires are left unconnected.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-knetwalk
%defattr(-,root,root,-)
%{tde_bindir}/knetwalk
%{tde_datadir}/apps/knetwalk
%{tde_datadir}/icons/hicolor/*/apps/knetwalk.png
%{tde_tdeappdir}/knetwalk.desktop
%{tde_tdedocdir}/HTML/en/knetwalk/
%{tde_mandir}/man*/knetwalk.*

##########

%package -n trinity-kolf
Summary:	Minigolf game for TDE
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kolf
This is a minigolf game for TDE that allows you to go through different
golf courses and waste an exorbitant amount of time.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kolf
%defattr(-,root,root,-)
%config(noreplace) %{tde_confdir}/magic/kolf.magic
%{tde_datadir}/apps/kolf/
%{tde_bindir}/kolf
%{tde_tdeappdir}/kolf.desktop
%{tde_datadir}/icons/hicolor/*/apps/kolf.png
%{tde_datadir}/mimelnk/application/x-kolf.desktop
%{tde_datadir}/mimelnk/application/x-kourse.desktop
%{tde_libdir}/libtdeinit_kolf.so
%{tde_libdir}/libtdeinit_kolf.la
%{tde_tdelibdir}/kolf.la
%{tde_tdelibdir}/kolf.so
%{tde_libdir}/libkolf.so.1
%{tde_libdir}/libkolf.so.1.2.0
%{tde_tdedocdir}/HTML/en/kolf/
%config(noreplace) %{tde_confdir}/magic/kolf.magic.mgc
%{tde_mandir}/man*/kolf.*

##########

%package -n trinity-kolf-devel
Summary:	Development files for Kolf
Group:		Development/Libraries/Other
Requires:	trinity-kolf = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kolf-devel
This package contains headers and development libraries for compiling
Kolf plugins.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kolf-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kolf
%{tde_libdir}/libkolf.la
%{tde_libdir}/libkolf.so

##########

%package -n trinity-konquest
Summary:	TDE based GNU-Lactic Konquest game
Group:		Amusements/Games/Strategy/Other

%description -n trinity-konquest
This the TDE version of Gnu-Lactic Konquest, a multi-player strategy
game. The goal of the game is to expand your interstellar empire
across the galaxy and, of course, crush your rivals in the process.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-konquest
%defattr(-,root,root,-)
%{tde_datadir}/apps/konquest/
%{tde_datadir}/icons/hicolor/*/apps/konquest.png
%{tde_tdeappdir}/konquest.desktop
%{tde_bindir}/konquest
%{tde_tdedocdir}/HTML/en/konquest/
%{tde_mandir}/man*/konquest.*

##########

%package -n trinity-kpat
Summary:	Trinity solitaire patience game
Group:		Amusements/Games/Board/Card

%description -n trinity-kpat
KPatience is a collection of 14 card games. All the games are single
player games.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kpat
%defattr(-,root,root,-)
%{tde_datadir}/icons/hicolor/*/apps/kpat.png
%{tde_datadir}/apps/kpat/
%{tde_tdeappdir}/kpat.desktop
%{tde_bindir}/kpat
%{tde_tdedocdir}/HTML/en/kpat/
%{tde_mandir}/man*/kpat.*

##########

%package -n trinity-kpoker
Summary:	Trinity based Poker clone
Group:		Amusements/Games/Board/Card

%description -n trinity-kpoker
KPoker is a TDE compliant clone of those highly addictive pocket
video poker games which are sometimes called "Videopoker" as well.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kpoker
%defattr(-,root,root,-)
%{tde_datadir}/apps/kpoker/
%{tde_datadir}/icons/hicolor/*/apps/kpoker.png
%{tde_tdeappdir}/kpoker.desktop
%{tde_bindir}/kpoker
%{tde_tdedocdir}/HTML/en/kpoker/
%{tde_mandir}/man*/kpoker.*

##########

%package -n trinity-kreversi
Summary:	Reversi for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kreversi
Reversi is a simple strategy game that is played by two
players. There is only one type of piece - one side of it is black,
the other white. If a player captures a piece on the board, that
piece is turned and belongs to that player. The winner is the person
that has more pieces of his own color on the board and if there are
no more moves possible.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kreversi
%defattr(-,root,root,-)
%{tde_bindir}/kreversi
%{tde_tdeappdir}/kreversi.desktop
%{tde_datadir}/apps/kreversi/
%{tde_datadir}/config.kcfg/kreversi.kcfg
%{tde_datadir}/icons/crystalsvg/*/actions/lastmoves.png
%{tde_datadir}/icons/crystalsvg/*/actions/legalmoves.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/lastmoves.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/legalmoves.svgz
%{tde_datadir}/icons/hicolor/*/apps/kreversi.png
%{tde_tdedocdir}/HTML/en/kreversi/
%{tde_mandir}/man*/kreversi.*

##########

%package -n trinity-ksame
Summary:	SameGame for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the high score. It has
been inspired by SameGame, that is only famous on the Macintosh
platform.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksame
%defattr(-,root,root,-)
%{tde_bindir}/ksame
%{tde_datadir}/icons/hicolor/*/apps/ksame.png
%{tde_datadir}/apps/ksame/
%{tde_tdeappdir}/ksame.desktop
%{tde_tdedocdir}/HTML/en/ksame/
%{tde_mandir}/man*/ksame.*

##########

%package -n trinity-kshisen
Summary:	Shisen-Sho for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kshisen
KShisen-Sho is a single-player-game similar to Mahjongg and uses the
same set of tiles as Mahjongg.

The object of the game is to remove all tiles from the field.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kshisen
%defattr(-,root,root,-)
%{tde_datadir}/apps/kshisen/
%{tde_datadir}/config.kcfg/kshisen.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kshisen.png
%{tde_tdeappdir}/kshisen.desktop
%{tde_bindir}/kshisen
%{tde_tdedocdir}/HTML/en/kshisen/
%{tde_mandir}/man*/kshisen.*

##########

%package -n trinity-ksirtet
Summary:	Tetris and Puyo-Puyo games for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-ksirtet
This program is a clone of the well known game Tetris. You must fit
the falling pieces to form full lines. You can rotate and translate
the falling piece. The game ends when no more piece can fall ie when
your incomplete lines reach the top of the board.

Every time you have destroyed 10 lines, you gain a level and the
pieces fall quicker (exactly the piece falls from a line each
1/(1+level) second).

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksirtet
%defattr(-,root,root,-)
%{tde_tdeappdir}/ksirtet.desktop
%{tde_datadir}/icons/hicolor/*/apps/ksirtet.png
%{tde_datadir}/apps/ksirtet/
%{tde_bindir}/ksirtet
%{tde_datadir}/config.kcfg/ksirtet.kcfg
%{tde_tdedocdir}/HTML/en/ksirtet/
%{tde_mandir}/man*/ksirtet.*

##########

%package -n trinity-ksmiletris
Summary:	Tetris like game for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ksmiletris
This is a game with falling blocks composed of different types of
smilies. The object of the game is to "crack a smile" by guiding
blocks so there are two or more of the same symbol vertically.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksmiletris
%defattr(-,root,root,-)
%{tde_datadir}/apps/ksmiletris/
%{tde_datadir}/icons/hicolor/*/apps/ksmiletris.png
%{tde_tdeappdir}/ksmiletris.desktop
%{tde_bindir}/ksmiletris
%{tde_tdedocdir}/HTML/en/ksmiletris/
%{tde_mandir}/man*/ksmiletris.*

##########

%package -n trinity-ksnake
Summary:	Snake Race for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksnake
%defattr(-,root,root,-)
%{tde_datadir}/apps/ksnake/
%{tde_datadir}/config.kcfg/ksnake.kcfg
%{tde_datadir}/icons/hicolor/*/apps/ksnake.png
%{tde_tdeappdir}/ksnake.desktop
%{tde_bindir}/ksnake
%{tde_tdedocdir}/HTML/en/ksnake/
%{tde_mandir}/man*/ksnake.*

##########

%package -n trinity-ksokoban
Summary:	Sokoban game for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-ksokoban
The first sokoban game was created in 1982 by Hiroyuki Imabayashi at
the Japanese company Thinking Rabbit, Inc. "Sokoban" is japanese for
"warehouse keeper". The idea is that you are a warehouse keeper
trying to push crates to their proper locations in a warehouse.

The problem is that you cannot pull the crates or step over them. If
you are not careful, some of the crates can get stuck in wrong places
and/or block your way.

It can be rather difficult just to solve a level. But if you want to
make it even harder, you can try to minimise the number of moves
and/or pushes you use to solve the level.

To make the game more fun for small kids (below 10 years or so), some
collections with easier levels are also included in KSokoban. These
are marked (easy) in the level collection menu. Of course, these
levels can be fun for adults too, for example if you don't want to
expose yourself to too much mental strain.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksokoban
%defattr(-,root,root,-)
%{tde_tdeappdir}/ksokoban.desktop
%{tde_datadir}/icons/hicolor/*/apps/ksokoban.png
%{tde_bindir}/ksokoban
%{tde_tdedocdir}/HTML/en/ksokoban/
%{tde_mandir}/man*/ksokoban.*

##########

%package -n trinity-kspaceduel
Summary:	Arcade two-player space game for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kspaceduel
KSpaceduel is an space arcade game for two players.

Each player controls a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kspaceduel
%defattr(-,root,root,-)
%{tde_datadir}/apps/kspaceduel/
%{tde_datadir}/icons/hicolor/*/apps/kspaceduel.png
%{tde_tdeappdir}/kspaceduel.desktop
%{tde_bindir}/kspaceduel
%{tde_datadir}/config.kcfg/kspaceduel.kcfg
%{tde_tdedocdir}/HTML/en/kspaceduel/
%{tde_mandir}/man*/kspaceduel.*

##########

%package -n trinity-ktron
Summary:	Tron clone for the K Desktop Environment
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ktron
The object of the game is to avoid running into walls, your own tail,
and that of your opponent.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ktron
%defattr(-,root,root,-)
%{tde_bindir}/ktron
%{tde_datadir}/icons/hicolor/*/apps/ktron.png
%{tde_tdeappdir}/ktron.desktop
%{tde_datadir}/apps/ktron/
%{tde_datadir}/config.kcfg/ktron.kcfg
%{tde_tdedocdir}/HTML/en/ktron/
%{tde_mandir}/man*/ktron.*

##########

%package -n trinity-ktuberling
Summary:	Potato Guy for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ktuberling
KTuberling is a game intended for small children. Of course, it may
be suitable for adults who have remained young at heart.

It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto a
potato-like guy.  Similarly, you have a penguin on which you can drop
other stuff.

There is no winner for the game. The only purpose is to make the
funniest faces you can.

There is a museum (like a "Madame Tusseau" gallery) where you can
find many funny examples of decorated potatoes. Of course, you can
send your own creations to the programmer, Eric Bischoff, who will
include them in the museum if he gets some spare time.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ktuberling
%defattr(-,root,root,-)
%{tde_bindir}/ktuberling
%{tde_datadir}/icons/hicolor/*/apps/ktuberling.png
%{tde_tdeappdir}/ktuberling.desktop
%{tde_datadir}/apps/ktuberling/
%{tde_datadir}/mimelnk/application/x-tuberling.desktop
%{tde_tdedocdir}/HTML/en/ktuberling/
%{tde_mandir}/man*/ktuberling.*

##########

%package -n trinity-twin4
Summary:	Connect Four clone for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-twin4
Four wins is a game for two players. Each player is represented by a
colour (yellow and red). The goal of the game is to get four
connected pieces of your colour into a row, column or any
diagonal. This is done by placing one of your pieces into any of the
seven columns. A piece will begin to fill a column from the bottom,
i.e. it will fall down until it reaches the ground level or another
stone. After a move is done it is the turn of the other player. This
is repeated until the game is over, i.e. one of the players has four
pieces in a row, column or diagonal or no more moves are possible
because the board is filled.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-twin4
%defattr(-,root,root,-)
%{tde_bindir}/twin4
%{tde_bindir}/twin4proc
%{tde_datadir}/apps/twin4/
%{tde_datadir}/config.kcfg/twin4.kcfg
%{tde_datadir}/icons/hicolor/*/apps/twin4.png
%{tde_tdeappdir}/twin4.desktop
%{tde_tdedocdir}/HTML/en/twin4/
%{tde_mandir}/man*/twin4.*
%{tde_mandir}/man*/twin4proc.*

##########

%package -n trinity-lskat
Summary:	Lieutnant Skat card game for Trinity
Group:		Amusements/Games/Board/Card

%description -n trinity-lskat
Lieutnant Skat (from German Offiziersskat) is a card game for two
players. It is roughly played according to the rules of Skat but with
only two players and simplified rules.

Every player has a set of cards in front of him/her, half of them
covered and half of them open. Both players try to win more than 60
of the 120 possible points. After 16 moves all cards are played and
the game ends.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-lskat
%defattr(-,root,root,-)
%{tde_bindir}/lskat
%{tde_bindir}/lskatproc
%{tde_datadir}/apps/lskat/
%{tde_datadir}/icons/hicolor/*/apps/lskat.png
%{tde_tdeappdir}/lskat.desktop
%{tde_tdedocdir}/HTML/en/lskat/
%{tde_mandir}/man*/lskat.*
%{tde_mandir}/man*/lskatproc.*

##########

%package -n trinity-tdefifteen
Summary:	Puzzle-solving game for Trinity
Group:		Amusements/Games

%description -n trinity-tdefifteen
TDEFifteen is a sliding puzzle that consists of a frame of numbered square
tiles in random order with one tile missing.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-tdefifteen
%defattr(-,root,root,-)
%{tde_bindir}/tdefifteen
%{tde_tdeappdir}/tdefifteen.desktop
%{tde_datadir}/icons/hicolor/*/apps/tdefifteen.png
%{tde_mandir}/man*/tdefifteen.*

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Specific path for RHEL4
if [ -d "/usr/X11R6" ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

if ! rpm -E %%cmake|grep -e 'cd build\|cd ${CMAKE_BUILD_DIR:-build}'; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DCMAKE_PROGRAM_PATH="%{tde_bindir}" \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DBUILD_ALL="ON" \
  -DWITH_ALL_OPTIONS="ON" \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{?buildroot} -C build

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file -r kasteroids      Game ArcadeGame
%suse_update_desktop_file -r KGoldrunner     Game ArcadeGame
%suse_update_desktop_file -r ksnake          Game ArcadeGame
%suse_update_desktop_file -r kspaceduel      Game ArcadeGame
%suse_update_desktop_file -r ktron           Game ArcadeGame
%suse_update_desktop_file -r kfouleggs       Game BlocksGame
%suse_update_desktop_file -r ksirtet         Game BlocksGame
%suse_update_desktop_file -r klickety        Game BoardGame
%suse_update_desktop_file -r ksmiletris      Game BlocksGame
%suse_update_desktop_file -r ktuberling      Game KidsGame
%suse_update_desktop_file -r atlantik        Game BoardGame
%suse_update_desktop_file -r kbackgammon     Game BoardGame
%suse_update_desktop_file -r kbattleship     Game BoardGame
%suse_update_desktop_file -r kblackbox       Game BoardGame
%suse_update_desktop_file -r kenolaba        Game BoardGame
%suse_update_desktop_file -r kmahjongg       Game BoardGame
%suse_update_desktop_file -r kreversi        Game BoardGame
%suse_update_desktop_file -r kshisen         Game BoardGame
%suse_update_desktop_file -r twin4           Game BoardGame
%suse_update_desktop_file -r kpat            Game CardGame
%suse_update_desktop_file -r kpoker          Game CardGame
%suse_update_desktop_file -r lskat           Game CardGame
%suse_update_desktop_file -r katomic         Game LogicGame
%suse_update_desktop_file -r kjumpingcube    Game LogicGame
%suse_update_desktop_file -r klines          Game LogicGame
%suse_update_desktop_file -r -G "Tactical Game" knetwalk Game LogicGame
%suse_update_desktop_file -r kmines          Game LogicGame
%suse_update_desktop_file -r konquest        Game LogicGame
%suse_update_desktop_file -r ksame           Game LogicGame
%suse_update_desktop_file -r ksokoban        Game LogicGame
%suse_update_desktop_file -r kbounce         Game LogicGame
%suse_update_desktop_file -r kolf            Game SportsGame
%endif

# Links duplicate files
%fdupes "%{?buildroot}"


%clean
%__rm -rf %{buildroot}


%changelog
