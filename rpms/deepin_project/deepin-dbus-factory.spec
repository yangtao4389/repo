# include old dbus-factory qml components for now, for compatibility
# https://git.archlinux.org/svntogit/community.git/commit/trunk/PKGBUILD?h=packages/deepin-qml-widgets&id=cbfd0d6ef4cdd63ff9b17d009302341ec07dc99a
%global project dbus-factory
%global repo %{project}

%global commit 0ef92677c266a9b5c76651f00e21bf94b9dae56f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global old_commit 5fe5f076b17d699de1dd04625a6b35e156a40efa
%global old_scommit %(c=%{old_commit}; echo ${c:0:7})

# for fedora 24
%global _qt5_qmldir %{_qt5_archdatadir}/qml

Name:           deepin-%{repo}
Version:        3.1.6
Release:        1.git%{shortcommit}%{?dist}
Summary:        Golang and QML DBus factory for DDE

Group:          Development/Libraries
License:        GPLv3
URL:            https://github.com/linuxdeepin/dbus-factory
Source0:        %{url}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
Source1:        %{url}/archive/%{old_commit}/%{repo}-%{old_scommit}.tar.gz

BuildRequires:  gcc-go
BuildRequires:  deepin-go-lib
BuildRequires:  deepin-dbus-generator
# For dbus-factory 3.0.6
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwebkit-devel

%description
Golang and QML DBus factory for DDE.

%package -n deepin-go-%{repo}
Summary: Golang DBus factory for DDE
%description -n deepin-go-%{repo}
Golang DBus factory for DDE

%package -n deepin-qml-%{repo}
Summary: QML DBus factory for DDE
%description -n deepin-qml-%{repo}
QML DBus factory for DDE.

%prep
%setup -q -a1 -n %{repo}-%{commit}
mv %{repo}-%{old_commit} old

%build
%make_build
%make_build build-qml -C old

%install
%make_install GOPATH=%{gopath}
make install-qml DESTDIR=%{buildroot} QT5_LIBDIR=%{_qt5_prefix} -C old

%files -n deepin-go-%{repo}
%doc README.md
%license LICENSE
%{gopath}/src/dbus/

%files -n deepin-qml-%{repo}
%doc README.md
%license LICENSE
%{_qt5_qmldir}/DBus/

%changelog
* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.6-1.git0ef9267
- Update to 3.1.6
* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.4-1.git2308ee3
- Update to 3.1.4
* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.0-1.git1fb380c
- Update to 3.1.0
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.9-1.git247464a
- Update to 3.0.9
* Sun Jul  5 2015 mosquito <sensor.wen@gmail.com> - 2.90.0-1.git402c0f2
- Update version to 2.90.0-1.git402c0f2
* Mon Sep 29 2014 mosquito <sensor.wen@gmail.com> - 0.0.2git20140928-1
- Initial build
