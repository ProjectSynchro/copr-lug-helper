Name:           lug-helper
Version:        3.1
Release:        2
Summary:        This script is designed to help you manage and optimize Star Citizen on Linux.

# SPDX
License:        GPL-3.0-only
URL:            https://starcitizen-lug.github.io
Source0:        https://github.com/starcitizen-lug/lug-helper/archive/refs/tags/v%{version}.tar.gz

Source1:        https://raw.githubusercontent.com/starcitizen-lug/lug-helper/d43b92d866b135c66a428edf1431c0019e4f2eed/lug-logo.png
Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       polkit
Requires:       winetricks

# Soft dependency for Zenity and Wine, optional but recommended.
Recommends:     zenity
Recommends:     wine

BuildArch: noarch

%description
The %{name} package contains the lug-helper script which is 
designed to help you manage and optimize Star Citizen on Linux.

%prep
%autosetup -p1 -n %{name}-%{version}
cp %{_sourcedir}/lug-logo.png %{_builddir}/%{name}-%{version}

%build
# No specific build steps

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications

# Copy files to their appropriate destinations
install -m 0755 %{_builddir}/%{name}-%{version}/%{name}.sh %{buildroot}%{_bindir}/%{name}
install -m 0644 %{_builddir}/%{name}-%{version}/lug-logo.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/lug-logo.png
install -m 0644 %{_builddir}/%{name}-%{version}/rsi-launcher.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/rsi-launcher.png
install -m 0644 %{_builddir}/%{name}-%{version}/lib/lutris-starcitizen.json %{buildroot}%{_datadir}/%{name}/lutris-starcitizen.json
install -m 0755 %{_builddir}/%{name}-%{version}/lib/sc-launch.sh %{buildroot}%{_datadir}/%{name}/sc-launch.sh

# Create desktop file
echo "[Desktop Entry]
Exec=%{name}
Icon=lug-logo.png
Name=LUG-Helper
StartupNotify=true
Terminal=true
Type=Application
Categories=Game" > %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
