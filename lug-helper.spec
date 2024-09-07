Name:           lug-helper
Version:        2.18
Release:        %autorelease
Summary:        This script is designed to help you manage and optimize Star Citizen on Linux.

# SPDX
License:        GPL-3.0-only
URL:            https://starcitizen-lug.github.io
Source0:        https://github.com/starcitizen-lug/lug-helper/archive/refs/tags/v%{version}.tar.gz

Requires:  bash
Requires:  coreutils
Requires:  curl
Requires:  polkit
Requires:  zenity

BuildArch: noarch

%description
The %{name} package contains the lug-helper script which is 
designed to help you manage and optimize Star Citizen on Linux.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# No specific build steps

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/192x192/apps
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications

# Copy files to their appropriate destinations
install -m 0755 %{_builddir}/%{name}-%{version}/%{name}.sh %{buildroot}%{_bindir}/%{name}
install -m 0644 %{_builddir}/%{name}-%{version}/lug-logo.png %{buildroot}%{_datadir}/icons/hicolor/192x192/apps/%{name}.png
install -m 0644 %{_builddir}/%{name}-%{version}/lib/lutris-starcitizen.json %{buildroot}%{_datadir}/%{name}/lutris-starcitizen.json

# Create desktop file
echo "[Desktop Entry]
Exec=%{name}
Icon=%{name}
Name=LUG-Helper
StartupNotify=true
Terminal=false
Type=Application
Categories=Game" > %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/192x192/apps/%{name}.png
%{_datadir}/%{name}/lutris-starcitizen.json
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog