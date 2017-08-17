%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name lodash.isarguments

Summary:       The modern build of lodash’s _.isArguments as a module.
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:        3.1.0
Release:        2%{?dist}
License:       MIT
URL:           https://github.com/lodash/lodash
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
The modern build of lodash’s _.isArguments as a module.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.0-2
- rh-nodejs8 rebuild

* Mon Oct 31 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.0-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.4-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.4-4
- Rebuilt with updated metapackage

* Fri Feb 12 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.4-3
- Rebuilt for RHSCL 2.2

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.4-2
- Enable scl macros, fix license macro for el6

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 3.0.4-1
- Initial package
