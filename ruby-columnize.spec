%define pkgname columnize
Summary:	Extracts common modeling concerns from ActiveRecord
Name:		ruby-%{pkgname}
Version:	0.3.2
Release:	1
License:	Ruby-alike
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	0b9031eea736d6822b60335ead7388f8
Group:		Development/Languages
URL:		http://rubyforge.org/projects/ruby-columnize/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In showing a long lists, sometimes one would prefer to see the value arranged aligned in columns. Some examples include listing methods of an object or debugger commands.

%package rdoc
Summary:	Documentation files for %{name}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%{ruby_rubylibdir}/columnize.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
#%{ruby_ridir}/LineCache
