Name: javax.jws
Version: 1.1
Release: 1
Group: Development/Java
Summary: An implementation of the javax.jws Web Services API
Source0: https://repo1.maven.org/maven2/javax/jws/javax.jws-api/%{version}/javax.jws-api-%{version}-sources.jar
Source1: https://repo1.maven.org/maven2/javax/jws/javax.jws-api/%{version}/javax.jws-api-%{version}.pom
License: BSD
BuildRequires: jdk-current
BuildRequires: javapackages-local
BuildArch: noarch

%description
An implementation of the javax.jws Web Services API

%prep
%autosetup -p1 -c %{name}-%{version}

%build
. %{_sysconfdir}/profile.d/90java.sh
export PATH=$JAVA_HOME/bin:$PATH

find . -name "*.java" |xargs javac --add-modules=java.activation,java.desktop -p %{_javadir}
find javax -name "*.class" -o -name "*.properties" |xargs jar cf javax.jws-%{version}.jar module-info.class META-INF
cp %{S:1} javax.jws-%{version}.pom

%install
mkdir -p %{buildroot}%{_javadir} %{buildroot}%{_mavenpomdir}
cp javax.jws-%{version}.jar %{buildroot}%{_javadir}
cp *.pom %{buildroot}%{_mavenpomdir}/
%add_maven_depmap javax.jws-%{version}.pom javax.jws-%{version}.jar

%files -f .mfiles
%{_javadir}/*.jar
