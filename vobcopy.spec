# 
# _with_lfs	enable largefile support (for files larger than 2GB)

Summary:	tool to copy selected titles from dvd to disk
Summary(pl):	program do kopiowania wybranych tytu³ów z dvd na dysk
Name:		vobcopy
Version:	0.5.5
Release:	2
License:	GPL
Group:		Applications
Source0:	http://lpn.rnbhq.org/download/%{name}-%{version}.tar.bz2
URL:		http://www.linux-programming-newbie.org/projects/c/c.html
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

Vobcopy pozwala na skopiowanie z DVD plików wideo przepakowanych fizycznie
na nowo, tak aby ka¿dy logiczny ci±g wideo (e.g. jeden odcinek serialu na
p³ycie na której s± cztery) by³ w jednym pliku (lub ich ci±gu), gotowy do
u¿ycia przez programy do obróbki wideo.

%description -l pl

Vobcopy lets you copy video files from DVD to disk in such a way that each
logical video stream (e.g. episode of a series on disc where are four of
these) is copied to one file, ready to use by video editing tools.

%prep
%setup -q

%build

sh ./configure
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
%doc README Changelog FAQ TODO Release-Notes *.txt
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*
