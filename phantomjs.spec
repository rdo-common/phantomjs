Name:           phantomjs
Version:        1.9.7
Release:        3%{?dist}
Summary:        Scriptable Headless WebKit

License:        BSD
URL:            http://phantomjs.org/
Source0:        https://github.com/ariya/phantomjs/archive/1.9.7/phantomjs-1.9.7.tar.gz

Patch0:		ignore-bundled-sqlite.patch

BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gperf
BuildRequires:  ruby
BuildRequires:  openssl-devel
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libicu-devel
BuildRequires:  sqlite-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel

Requires: sqlite

%description
PhantomJS is a headless WebKit scriptable with a JavaScript API. It has fast and
native support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG.

%prep
%setup -q
%patch0 -p1


%build
./build.sh --confirm --jobs 4 --qt-config "-system-sqlite"

%install
mkdir -p %{buildroot}%{_bindir}
cp bin/phantomjs %{buildroot}%{_bindir}
chrpath -d %{buildroot}%{_bindir}/phantomjs


%files
%attr(755, root, root) %{_bindir}/phantomjs


%changelog
* Fri Jul 31 2015 Lon Hohberger <lhh@redhat.com> 1.9.7-3
- Use system-sqlite instead of bundled sqlite

* Wed Jul 29 2015 Graeme Gillies <ggillies@redhat.com> - 1.9.7-1
- Initial Packaging
