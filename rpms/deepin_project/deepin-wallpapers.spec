%global commit 3e5c89d5464e9e5a254c58e09a75ded0fce5dcd6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           deepin-wallpapers
Version:        1.6
Release:        1.git%{shortcommit}%{?dist}
Summary:        Deepin Wallpapers provides wallpapers of dde
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Deepin Wallpapers provides wallpapers of dde

%prep
%setup -q -n %{name}-%{commit}

%build

%install
install -d %{buildroot}/%{_datadir}/wallpapers/
cp -r deepin %{buildroot}/%{_datadir}/wallpapers/

install -d %{buildroot}/%{_var}/cache/
cp -r image-blur %{buildroot}/%{_var}/cache/

%files
%doc README.md
%{_datadir}/wallpapers/deepin/
%{_var}/cache/image-blur/

%changelog
* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.6-1.git3e5c89d
- Update to 1.6
* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.4-1.gita54c282
- Update to 1.4
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.3-1.gitdbc981b
- Update to 1.3
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build
