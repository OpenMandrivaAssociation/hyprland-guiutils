Name:		hyprland-guiutils
Version:	0.2.1
Release:	1
Source0:	https://github.com/hyprwm/hyprland-guiutils/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	Hyprland GUI utilities
URL:		https://github.com/hyprwm/hyprland-guiutils
License:	BSD-3-Clause
Group:		Window Manager/Hyprland/Utility

BuildSystem:	cmake

BuildRequires:	cmake
BuildRequires:  pkgconfig(aquamarine) >= 0.9.5
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprgraphics) >= 0.2.0
BuildRequires:	pkgconfig(hyprlang) >= 0.6.0
BuildRequires:	pkgconfig(hyprutils) >= 0.2.4
BuildRequires:	pkgconfig(hyprtoolkit) >= 0.2.2
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
