from pathlib import Path
import sys,difflib
src=Path(sys.argv[1]);old=src.read_text();s=old
extra=(Path(__file__).with_name('nr_packets_48b.cc.inc')).read_text()
s=s.replace('int\nmain(int argc, char* argv[])',extra+'\nint\nmain(int argc, char* argv[])')
s=s.replace('#include "ns3/applications-module.h"','#include "ns3/applications-module.h"\n#include <cstring>')
s=s.replace('uint16_t ueNum = 2;','uint16_t ueNum = 4;').replace('uint16_t interUeDistance = 20;','uint16_t interUeDistance = 35;').replace('Time simTime = Seconds(10);','Time simTime = Seconds(20);')
s=s.replace('CommandLine cmd(__FILE__);','bool activeOnly=false;\n    CommandLine cmd(__FILE__);\n    cmd.AddValue("activeOnly","C1 active-only data service, with fixed metadata frames",activeOnly);')
s=s.replace('ns3::ConstantPositionMobilityModel','ns3::ConstantVelocityMobilityModel').replace('mobility.Install(ueVoiceContainer);','mobility.Install(ueVoiceContainer);\n    for(uint32_t n=0;n<4;++n)ueVoiceContainer.Get(n)->GetObject<ConstantVelocityMobilityModel>()->SetVelocity(Vector(25,0,0));')
a=s.index('    // Set Application in the UEs');b=s.index('    // Datebase setup',a)
s=s[:a]+r"""
    NS_ABORT_MSG_IF(useIPv6,"CEP13 trace configuration is IPv4 only");
    cepEvents.open(outputDir+simTag+"-events.csv");cepEvents<<"event,time_ns,link,type,generation,seq,node,app_bytes\n";
    ApplicationContainer clientApps,serverApps; // Original application trace loops remain empty.
    std::vector<Ptr<Socket>> cepSockets;
    for(uint32_t n=0;n<4;++n){auto sock=Socket::CreateSocket(ueVoiceContainer.Get(n),UdpSocketFactory::GetTypeId());sock->Bind(localAddress);sock->Connect(remoteAddress);sock->SetRecvCallback(MakeBoundCallback(&CepReceive,n));cepSockets.push_back(sock);}
    uint32_t seq=0;const int phases[3]={0,0,1};
    for(int g=-6;g<180;++g){double t=3.0+g*0.1;Simulator::Schedule(Seconds(t+.0001),&CepSend,cepSockets[0],uint8_t(0),uint8_t(255),int64_t(g),seq++);
      for(int link=0;link<3;++link){if(activeOnly&&link==0)continue;if(((g%3)+3)%3==phases[link])Simulator::Schedule(Seconds(t+.002),&CepSend,cepSockets[link],uint8_t(1),uint8_t(link),int64_t(g),seq++);}}
    double realAppStart=2.4;
"""+s[b:]
s=s.replace('    Simulator::Destroy();','    cepEvents.close();\n    Simulator::Destroy();')
assert s!=old;src.write_text(s);Path('results/network/source.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='official.cc',tofile='cep13.cc')))