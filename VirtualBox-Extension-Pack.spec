Name: VirtualBox-Extension-Pack
%define version 6.1.38
Version: %{version}
Release: 1
Summary: VirtualBox Extensions Pack
License: Oracle
Source0: Oracle_VM_VirtualBox_Extension_Pack-%{version}.vbox-extpack
ExclusiveArch: x86_64
BuildRoot: %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _enable_debug_packages 0

%description
Virtualbox Extensions Pack

%prep
%setup -qcT
%{__tar} -zxf %{SOURCE0}

%install
install -d $RPM_BUILD_ROOT/usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
cp -a linux.amd64 $RPM_BUILD_ROOT/usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
install -p PXE-Intel.rom $RPM_BUILD_ROOT/usr/lib64//virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
install -p ExtPack.xml $RPM_BUILD_ROOT/usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack

%files
%defattr(644,root,root,755)
%dir /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack
%dir /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxEhciR0.r0
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxEhciR3.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxHostWebcam.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxNvmeR0.r0
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxNvmeR3.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxPuelMain.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxPuelMainVM.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxUsbCardReaderR3.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxUsbWebcamR3.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VBoxVRDP.so
%attr(755,root,root) /usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/linux.amd64/VDPluginCrypt.so
/usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/PXE-Intel.rom
/usr/lib64/virtualbox/ExtensionPacks/Oracle_VM_VirtualBox_Extension_Pack/ExtPack.xml
