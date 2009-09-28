### RPM external pyqt 4.5
## INITENV +PATH PYTHONPATH %i/lib/python2.4/site-packages
## BUILDIF case %cmsplatf in osx*) false;; *) true;; esac
Source: http://www.riverbankcomputing.co.uk/static/Downloads/PyQt4/PyQt-x11-gpl-%realversion.tar.gz
Requires: python
Requires: qt
Requires: sip

%prep
%setup -n PyQt-x11-gpl-%realversion

%build
echo yes | python ./configure.py -b %i/bin -d %i/lib/python`echo $PYTHON_VERSION | cut -d. -f 1,2`/site-packages -e %i/include --no-sip-files --no-designer-plugin
make %makeprocesses

%install
make install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/pyqt
<doc type=BuildSystem::ToolDoc version=1.0>
<Tool name=pyqt version=%v>
<info url="http://www.riverbankcomputing.co.uk/software/pyqt/intro"></info>
<Client>
 <Environment name=PYQT_BASE default="%i"></Environment>
 <Environment name=PYTHONPATH default="$PYQT_BASE/lib/python2.4/site-packages"></Environment>
</Client>
<Runtime name=PYTHONPATH value="$PYQT_BASE/lib/python2.4/site-packages" type=path>
<use name="python">
<use name="qt">
</Tool>
EOF_TOOLFILE

%post
%{relocateConfig}etc/scram.d/pyqt
