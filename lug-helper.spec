%global tag 4.2

Name:           lug-helper
Version:        %{tag}
Release:        1.%{lua:print(os.date('%Y%m%d'))}%{?dist}
Summary:        This script is designed to help you manage and optimize Star Citizen on Linux.

# SPDX
License:        GPL-3.0-only
URL:            https://starcitizen-lug.github.io
Source0:        https://github.com/starcitizen-lug/lug-helper/archive/refs/tags/v%{version}.tar.gz

Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       polkit
Requires:       zenity

# Winetricks dependencies
Requires:       cabextract 
Requires:       gzip 
Requires:       unzip 
Requires:       wget 
Requires:       which
Requires:       hicolor-icon-theme

# Soft dependency for system Wine, optional but recommended.
Recommends:     wine

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
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications

# Copy main script
install -m 0755 %{_builddir}/%{name}-%{version}/%{name}.sh %{buildroot}%{_bindir}/%{name}

# Copy all PNG icons
install -m 0644 %{_builddir}/%{name}-%{version}/*.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

# Copy all files from lib directory as regular files
find %{_builddir}/%{name}-%{version}/lib -type f ! -name 'sc-launch.sh' -exec install -m 0644 {} %{buildroot}%{_datadir}/%{name}/ \;

# Ensure sc-launch.sh is executable
install -m 0755 %{_builddir}/%{name}-%{version}/lib/sc-launch.sh %{buildroot}%{_datadir}/%{name}/

# Create desktop file
echo "[Desktop Entry]
Exec=%{name}
Icon=lug-logo.png
Name=LUG-Helper
StartupNotify=true
Terminal=false
Type=Application
Categories=Game" > %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/256x256/apps/*.png
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
