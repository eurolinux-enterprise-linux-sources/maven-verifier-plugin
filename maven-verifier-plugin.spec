Name:           maven-verifier-plugin
Version:        1.0
Release:        10%{?dist}
Summary:        Maven Verifier Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-verifier-plugin/
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-verifier-plugin-1.0/
#tar -zcf maven-verifier-plugin-1.0.tar.gz maven-verifier-plugin-1.0/
Source0:        %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: junit
BuildRequires: plexus-utils
BuildRequires: maven-surefire-provider-junit

Requires: maven
Requires: java
Requires: jpackage-utils
Requires: junit
Requires: plexus-utils

Obsoletes: maven2-plugin-verifier <= 0:2.0.8
Provides: maven2-plugin-verifier = 1:%{version}-%{release}

%description
Assists in integration testing by means of evaluating 
success/error conditions read from a configuration file.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.


%prep
%setup -q 

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar  %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-10
- Mass rebuild 2013-12-27

* Thu Nov  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-9
- Remove legacy Maven macros

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-4
- Build with maven v3.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Hui Wang <huwang@redhat.com> - 1.0-2
- Add missing requires maven2

* Wed Jun 02 2010 Hui Wang <huwang@redhat.com> - 1.0-1
- Initial version of the package
