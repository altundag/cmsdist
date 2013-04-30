### RPM cms coral-tool-conf 2.1
## NOCOMPILER
%define isnotonline %(case %{cmsplatf} in (*onl_*_*) echo 0 ;; (*) echo 1 ;; esac)

Requires: pcre-toolfile
Requires: python-toolfile
Requires: expat-toolfile
Requires: boost-toolfile
Requires: frontier_client-toolfile
Requires: gcc-toolfile
Requires: openssl-toolfile

%if %isnotonline
Requires: sqlite-toolfile
Requires: libuuid-toolfile
Requires: zlib-toolfile
Requires: cppunit-toolfile
Requires: xerces-c-toolfile
%ifarch  i386 i486 i585 i686 x86_64
Requires: oracle-toolfile
%endif
Requires: systemtools
%else
Requires: onlinesystemtools
%define onlinesystemtoolsroot ${ONLINESYSTEMTOOLS_ROOT}
%endif

%define skipreqtools jcompiler boost_python

## IMPORT scramv1-tool-conf