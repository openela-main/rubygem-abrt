# Generated from abrt-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name abrt

Name: rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: ABRT support for Ruby
License: MIT
URL: http://github.com/voxik/abrt-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/voxik/abrt-ruby.git && cd abrt-ruby
# git archive -v -o abrt-0.4.0-spec.tar.gz v0.4.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
Requires: libreport-filesystem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Provides ABRT reporting support for libraries/applications written using Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_sysconfdir}/libreport/events.d/
cp -a .%{gem_instdir}/config/ruby_event.conf %{buildroot}%{_sysconfdir}/libreport/events.d/


%check
pushd .%{gem_instdir}
cp -a %{_builddir}/spec spec

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%exclude %{gem_instdir}/config
%config(noreplace) %{_sysconfdir}/libreport/events.d/ruby_event.conf

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Wed Jun 24 2020 Jun Aruga <jaruga@redhat.com> - 0.4.0-1
- Update to abrt 0.4.0.
  Resolves: rhbz#1842476

* Tue Jul 31 2018 Vít Ondruch <vondruch@redhat.com> - 0.3.0-4
- Execute test suite unconditionally.
- Upload correct sources.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Vít Ondruch <vondruch@redhat.com> - 0.3.0-1
- Update to abrt 0.3.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Vít Ondruch <vondruch@redhat.com> - 0.2.0-1
- Update to abrt 0.2.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 01 2015 Vít Ondruch <vondruch@redhat.com> - 0.1.1-1
- Update to abrt 0.1.1.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.6-1
- Update to abrt 0.0.6.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.5-2
- Disable tests for EL builds.

* Mon May 06 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.5-1
- Update to abrt 0.0.5.

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.3-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 17 2012 Vít Ondruch <vondruch@redhat.com> - 0.0.3-1
- Update to abrt 0.0.3.

* Mon Jul 09 2012 Vít Ondruch <vondruch@redhat.com> - 0.0.2-1
- Initial package
