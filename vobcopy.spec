#
# _with_lfs	enable largefile support (for files larger than 2GB)

Summary:	Tool to copy selected titles from dvd to disk
Summary(pl):	Program do kopiowania wybranych tytu��w z dvd na dysk
Name:		vobcopy
Version:	0.5.7
Release:	1
License:	GPL
Group:		Applications
Source0:	http://lpn.rnbhq.org/download/%{name}-%{version}.tar.bz2
URL:		http://www.linux-programming-newbie.org/projects/c/c.html
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vobcopy lets you copy video files from DVD to disk in such a way that
each logical video stream (e.g. episode of a series on disc where are
four of these) is copied to one file, ready to use by video editing
tools.

%description -l pl
Vobcopy pozwala na skopiowanie z DVD plik�w wideo przepakowanych
fizycznie na nowo, tak aby ka�dy logiczny ci�g wideo (np. jeden
odcinek serialu na p�ycie na kt�rej s� cztery) by� w jednym pliku (lub
ich ci�gu), gotowy do u�ycia przez programy do obr�bki wideo.

%prep
%setup -q

%build
# lfs should be on by default?
./configure.sh %{?_with_lfs:--with-lfs}
%{__make} %{!?_with_lfs:disable_lfs}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

install vobcopy $RPM_BUILD_ROOT/%{_bindir}
install vobcopy.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog TODO Release-Notes *.txt
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*
