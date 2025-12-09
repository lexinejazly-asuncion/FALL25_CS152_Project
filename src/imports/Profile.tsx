function Text() {
  return (
    <div className="content-stretch flex items-start relative shrink-0" data-name="Text">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#757575] text-[16px] text-nowrap whitespace-pre">Here is a list of your recommended and saved clubs and organizations</p>
    </div>
  );
}

function Description() {
  return (
    <div className="absolute content-stretch flex flex-col gap-[4px] h-[55px] items-start left-[23px] top-[23px] w-[272px]" data-name="Description">
      <p className="font-['Inter:Semi_Bold',sans-serif] font-semibold leading-[1.2] min-w-full not-italic relative shrink-0 text-[#1e1e1e] text-[24px] tracking-[-0.48px] w-[min-content]">FoundYourRSOs</p>
      <Text />
    </div>
  );
}

function Suggestions() {
  return (
    <div className="absolute contents left-[23px] top-[104px]" data-name="Suggestions">
      <div className="absolute bg-[#f0f9fc] border border-[#757575] border-solid h-[59px] left-[24px] rounded-[5px] top-[105px] w-[434px]" />
      <p className="absolute font-['CantoraOne:Regular',sans-serif] leading-[30px] left-[calc(50%-306px)] not-italic text-[#1e1e1e] text-[24px] top-[120px] tracking-[-0.48px] w-[151.906px]">RSO Name</p>
    </div>
  );
}

function Suggestions1() {
  return (
    <div className="absolute contents left-[23px] top-[173px]" data-name="Suggestions">
      <div className="absolute bg-[#f0f9fc] border border-[#757575] border-solid h-[59px] left-[24px] rounded-[5px] top-[174px] w-[434px]" />
      <p className="absolute font-['CantoraOne:Regular',sans-serif] leading-[30px] left-[calc(50%-306px)] not-italic text-[#1e1e1e] text-[24px] top-[189px] tracking-[-0.48px] w-[151.906px]">RSO Name</p>
    </div>
  );
}

function Suggestions2() {
  return (
    <div className="absolute contents left-[23px] top-[242px]" data-name="Suggestions">
      <div className="absolute bg-[#f0f9fc] border border-[#757575] border-solid h-[59px] left-[24px] rounded-[5px] top-[243px] w-[434px]" />
      <p className="absolute font-['CantoraOne:Regular',sans-serif] leading-[30px] left-[calc(50%-306px)] not-italic text-[#1e1e1e] text-[24px] top-[258px] tracking-[-0.48px] w-[151.906px]">RSO Name</p>
    </div>
  );
}

function Suggestions3() {
  return (
    <div className="absolute contents left-[23px] top-[311px]" data-name="Suggestions">
      <div className="absolute bg-[#f0f9fc] border border-[#757575] border-solid h-[59px] left-[24px] rounded-[5px] top-[312px] w-[434px]" />
      <p className="absolute font-['CantoraOne:Regular',sans-serif] leading-[30px] left-[calc(50%-306px)] not-italic text-[#1e1e1e] text-[24px] top-[327px] tracking-[-0.48px] w-[151.906px]">RSO Name</p>
    </div>
  );
}

function Suggestions4() {
  return (
    <div className="absolute contents left-[23px] top-[380px]" data-name="Suggestions">
      <div className="absolute bg-[#f0f9fc] border border-[#757575] border-solid h-[59px] left-[24px] rounded-[5px] top-[381px] w-[434px]" />
      <p className="absolute font-['CantoraOne:Regular',sans-serif] leading-[30px] left-[calc(50%-306px)] not-italic text-[#1e1e1e] text-[24px] top-[396px] tracking-[-0.48px] w-[151.906px]">RSO Name</p>
    </div>
  );
}

function FormLogIn() {
  return (
    <div className="absolute bg-[#f5f8f9] border border-[#d9d9d9] border-solid h-[548px] left-[372px] rounded-[8px] top-[287px] w-[696px]" data-name="Form Log In">
      <Description />
      <Suggestions />
      <Suggestions1 />
      <Suggestions2 />
      <Suggestions3 />
      <Suggestions4 />
    </div>
  );
}

export default function Profile() {
  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec]" data-name="Profile">
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      <FormLogIn />
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-141px)] text-[48px] text-black text-nowrap top-[164px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        Hello, Name!
      </p>
      <div className="absolute bg-[#d9d9d9] h-[102px] left-[1031px] top-[386px] w-[4px]" />
    </div>
  );
}