Name:		hyprland-guiutils
Version:	0.2.2
Release:	2
Source0:	https://github.com/hyprwm/hyprland-guiutils/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	Hyprland GUI utilities
URL:		https://github.com/hyprwm/hyprland-guiutils
License:	BSD-3-Clause
Group:		Utility

BuildSystem:	cmake

BuildRequires:	cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(aquamarine) >= 0.9.5
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:	pkgconfig(hyprlang) >= 0.6.0
BuildRequires:	pkgconfig(hyprutils) >= 0.10.2
BuildRequires:	pkgconfig(hyprtoolkit) >= 0.4.0
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xkbcommon)

Obsoletes:      hyprland-qtutils

%description
Hyprland GUI utilities (successor to hyprland-qtutils)

%prep
%autosetup -p1

%files
%{_bindir}/hyprland-dialog
%{_bindir}/hyprland-donate-screen
%{_bindir}/hyprland-update-screen
%{_bindir}/hyprland-run
%{_bindir}/hyprland-welcome
