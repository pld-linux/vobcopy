#
# Conditional build:
%bcond_without	lfs	# disable largefile support (for files larger than 2GB)
#
Summary:	Tool to copy selected titles from dvd to disk
Summary(pl.UTF-8):	Program do kopiowania wybranych tytułów z dvd na dysk
Name:		vobcopy
Version:	1.1.2
Release:	2
License:	GPL
Group:		Applications
Source0:	http://lpn.rnbhq.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	7f4bc2ba19d567339e4d854636aafa24
URL:		http://www.linux-programming-newbie.org/projects/c/c.html
BuildRequires:	libdvdread-devel
Requires:	libdvdcss
Requires:	libdvdread
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vobcopy lets you copy video files from DVD to disk in such a way that
each logical video stream (e.g. episode of a series on disc where are
four of these) is copied to one file, ready to use by video editing
tools.

%description -l pl.UTF-8
Vobcopy pozwala na skopiowanie z DVD plików wideo przepakowanych
fizycznie na nowo, tak aby każdy logiczny ciąg wideo (np. jeden
odcinek serialu na płycie na której są cztery) był w jednym pliku (lub
ich ciągu), gotowy do użycia przez programy do obróbki wideo.

%prep
%setup -q

%build
sh configure.sh \
	%{?with_lfs:--with-lfs}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,de/man1}}

install vobcopy $RPM_BUILD_ROOT%{_bindir}
install vobcopy.1 $RPM_BUILD_ROOT%{_mandir}/man1
install vobcopy.1.de $RPM_BUILD_ROOT%{_mandir}/de/man1/vobcopy.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README Release-Notes *.txt TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
