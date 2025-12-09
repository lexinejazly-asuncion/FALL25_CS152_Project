function Text() {
  return (
    <div className="content-stretch flex items-start relative shrink-0" data-name="Text">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#757575] text-[16px] text-nowrap whitespace-pre">Tell us what you’re looking for, we’ll do the rest.</p>
    </div>
  );
}

function Description() {
  return (
    <div className="content-stretch flex flex-col gap-[4px] h-[55px] items-start relative shrink-0 w-[272px]" data-name="Description">
      <p className="font-['Inter:Semi_Bold',sans-serif] font-semibold leading-[1.2] min-w-full not-italic relative shrink-0 text-[#1e1e1e] text-[24px] tracking-[-0.48px] w-[min-content]">FindYourFit</p>
      <Text />
    </div>
  );
}

function ChevronDown() {
  return (
    <div className="relative shrink-0 size-[16px]" data-name="Chevron down">
      <svg className="block size-full" fill="none" preserveAspectRatio="none" viewBox="0 0 16 16">
        <g id="Chevron down">
          <path d="M4 6L8 10L12 6" id="Icon" stroke="var(--stroke-0, #1E1E1E)" strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.6" />
        </g>
      </svg>
    </div>
  );
}

function Select() {
  return (
    <div className="bg-white h-[40px] min-w-[240px] relative rounded-[8px] shrink-0 w-full" data-name="Select">
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-[-0.5px] pointer-events-none rounded-[8.5px]" />
      <div className="flex flex-row items-center min-w-[inherit] size-full">
        <div className="content-stretch flex gap-[8px] h-[40px] items-center min-w-[inherit] pl-[16px] pr-[12px] py-[12px] relative w-full">
          <p className="basis-0 font-['Inter:Regular',sans-serif] font-normal grow leading-none min-h-px min-w-px not-italic relative shrink-0 text-[#b3b3b3] text-[16px]">Value</p>
          <ChevronDown />
        </div>
      </div>
    </div>
  );
}

function Q1Type() {
  return (
    <div className="content-stretch flex flex-col gap-[8px] h-[69px] items-start relative shrink-0 w-[471px]" data-name="Q1. Type">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] min-w-full not-italic relative shrink-0 text-[#1e1e1e] text-[16px] w-[min-content]">What type of club/organization are you looking for?</p>
      <Select />
    </div>
  );
}

function Button() {
  return (
    <div className="basis-0 bg-[#576ce6] grow min-h-px min-w-px relative rounded-[8px] shrink-0" data-name="Button">
      <div className="flex flex-row items-center justify-center overflow-clip rounded-[inherit] size-full">
        <div className="content-stretch flex gap-[8px] items-center justify-center p-[12px] relative w-full">
          <p className="font-['Inter:Regular',sans-serif] font-normal leading-none not-italic relative shrink-0 text-[16px] text-neutral-100 text-nowrap whitespace-pre">Submit</p>
        </div>
      </div>
      <div aria-hidden="true" className="absolute border border-[#2c2c2c] border-solid inset-0 pointer-events-none rounded-[8px]" />
    </div>
  );
}

function Submit() {
  return (
    <div className="content-stretch flex gap-[16px] h-[27px] items-center relative shrink-0 w-[155px]" data-name="Submit">
      <Button />
    </div>
  );
}

function FormLogIn() {
  return (
    <div className="absolute bg-[#f5f8f9] content-stretch flex flex-col gap-[24px] h-[555px] items-start left-[242px] min-w-[320px] p-[24px] rounded-[8px] top-[199px] w-[956px]" data-name="Form Log In">
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-0 pointer-events-none rounded-[8px]" />
      <Description />
      <Q1Type />
      <Submit />
    </div>
  );
}

export default function FormPage() {
  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec]" data-name="Form Page">
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      <FormLogIn />
    </div>
  );
}