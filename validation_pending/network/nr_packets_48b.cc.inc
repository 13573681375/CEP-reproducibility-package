// CEP13 derivative of the GPL-2.0 NR-V2X example. Payload-independent one-way trace coupling.
#include <fstream>
#include <vector>
class CepHeader : public Header {
public:
 uint8_t type=0,link=0; int64_t generation=0; uint64_t generatedNs=0; uint32_t seq=0; double speed=25.0;
 static TypeId GetTypeId(){static TypeId t=TypeId("ns3::Cep13Header").SetParent<Header>().AddConstructor<CepHeader>();return t;}
 TypeId GetInstanceTypeId() const override{return GetTypeId();}
 uint32_t GetSerializedSize() const override{return 48;}
 void Serialize(Buffer::Iterator i) const override{ i.WriteHtonU32(0x43455031);i.WriteU8(type);i.WriteU8(link);i.WriteHtonU16(0);i.WriteHtonU64(static_cast<uint64_t>(generation));i.WriteHtonU64(generatedNs);i.WriteHtonU32(seq);i.WriteHtonU32(48);uint64_t bits;std::memcpy(&bits,&speed,8);i.WriteHtonU64(bits);i.WriteHtonU64(0); }
 uint32_t Deserialize(Buffer::Iterator i) override{NS_ABORT_MSG_IF(i.ReadNtohU32()!=0x43455031,"Bad CEP magic");type=i.ReadU8();link=i.ReadU8();i.ReadNtohU16();generation=static_cast<int64_t>(i.ReadNtohU64());generatedNs=i.ReadNtohU64();seq=i.ReadNtohU32();i.ReadNtohU32();uint64_t bits=i.ReadNtohU64();std::memcpy(&speed,&bits,8);i.ReadNtohU64();return 48;}
 void Print(std::ostream& os) const override{os<<"CEP13 "<<generation;}
};
std::ofstream cepEvents;
void CepSend(Ptr<Socket> socket,uint8_t type,uint8_t link,int64_t generation,uint32_t seq){
 CepHeader h;h.type=type;h.link=link;h.generation=generation;h.generatedNs=static_cast<uint64_t>((3.0+generation*0.1)*1e9+0.5);h.seq=seq;
 Ptr<Packet> p=Create<Packet>();p->AddHeader(h);int sent=socket->Send(p);
 cepEvents<<"tx,"<<Simulator::Now().GetNanoSeconds()<<","<<unsigned(link)<<","<<unsigned(type)<<","<<generation<<","<<seq<<","<<unsigned(type==0?0:link)<<","<<sent<<"\n";
 txPktCounter++;txByteCounter+=p->GetSize();
}
void CepReceive(uint32_t node,Ptr<Socket> socket){
 Address from;Ptr<Packet> p;while((p=socket->RecvFrom(from))){if(p->GetSize()<48)continue;CepHeader h;p->RemoveHeader(h);bool intended=(h.type==0?node>0:node==uint32_t(h.link+1));
 cepEvents<<"rx,"<<Simulator::Now().GetNanoSeconds()<<","<<unsigned(h.link)<<","<<unsigned(h.type)<<","<<h.generation<<","<<h.seq<<","<<node<<",48\n";
 if(intended){rxPktCounter++;rxByteCounter+=48;}}
}