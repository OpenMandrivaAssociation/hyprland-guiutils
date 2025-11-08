Name:		hyprland-guiutils
Version:	0.1.0
Release:	1
Source0:	https://github.com/hyprwm/hyprland-guiutils/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	Hyprland GUI utilities
URL:		https://github.com/hyprwm/hyprland-guiutils
License:	BSD-3-Clause
Group:		Window Manager/Hyprland/Utility

BuildSystem:	cmake

BuildRequires:	cmake
BuildRequires:	pkgconfig(hyprlang) >=0.6.0
BuildRequires:	pkgconfig(hyprutils) >=0.2.4
BuildRequires:	pkgconfig(hyprtoolkit) >=0.2.2
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(libdrm)

Obsoletes:      hyprland-qtutils

%description
Hyprland GUI utilities (successor to hyprland-qtutils)

%prep
%autosetup -p1

%files
