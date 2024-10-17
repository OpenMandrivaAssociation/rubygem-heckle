%define oname heckle

Summary:    Heckle is unit test sadism(tm) at it's core
Name:       rubygem-%{oname}
Version:    1.4.3
Release:    2
Group:      Development/Ruby
License:    MIT
URL:        https://www.rubyforge.org/projects/seattlerb
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(ParseTree) >= 2.0.0
Requires:   rubygem(ruby2ruby) >= 1.1.6
Requires:   rubygem(ZenTest) >= 3.5.2
Requires:   rubygem(hoe) >= 2.3.0
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Heckle is unit test sadism(tm) at it's core. Heckle is a mutation tester. It
modifies your code and runs your tests to make sure they fail. The idea is
that if code can be changed and your tests don't notice, either that code
isn't being covered or it doesn't do anything.
It's like hiring a white-hat hacker to try to break into your server and
making sure you detect it. You learn the most by trying to break things and
watching the outcome in an act of unit test sadism.

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x
ruby -pi -e 'sub(/\/usr\/local\/bin\/ruby/, "/usr/bin/env ruby")' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin/*

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/heckle
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.autotest
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/sample/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sun Oct 10 2010 Rémy Clouard <shikamaru@mandriva.org> 1.4.3-1mdv2011.0
+ Revision: 584523
- import rubygem-heckle

