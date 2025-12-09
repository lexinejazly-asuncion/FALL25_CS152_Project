import { useState } from 'react';

function Text() {
  return (
    <div className="content-stretch flex items-start relative shrink-0" data-name="Text">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#757575] text-[16px] text-nowrap whitespace-pre">Tell us what you&apos;re looking for, we&apos;ll do the rest.</p>
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

function TextInput({ value, onChange }: { value: string; onChange: (value: string) => void }) {
  return (
    <div className="bg-white h-[40px] min-w-[240px] relative rounded-[8px] shrink-0 w-full" data-name="Input">
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-[-0.5px] pointer-events-none rounded-[8.5px]" />
      <div className="flex flex-row items-center min-w-[inherit] size-full">
        <div className="content-stretch flex gap-[8px] h-[40px] items-center min-w-[inherit] pl-[16px] pr-[12px] py-[12px] relative w-full">
          <input
            type="text"
            value={value}
            onChange={(e) => onChange(e.target.value)}
            placeholder="Enter club/organization type"
            className="basis-0 font-['Inter:Regular',sans-serif] font-normal grow leading-none min-h-px min-w-px not-italic relative shrink-0 text-[#1e1e1e] text-[16px] placeholder:text-[#b3b3b3] bg-transparent border-none outline-none w-full"
          />
        </div>
      </div>
    </div>
  );
}

function Q1Type({ value, onChange }: { value: string; onChange: (value: string) => void }) {
  return (
    <div className="content-stretch flex flex-col gap-[8px] h-[69px] items-start relative shrink-0 w-[471px]" data-name="Q1. Type">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] min-w-full not-italic relative shrink-0 text-[#1e1e1e] text-[16px] w-[min-content]">What are you looking for in a club or organization?</p>
      <TextInput value={value} onChange={onChange} />
    </div>
  );
}

function Button({ onClick }: { onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="basis-0 bg-[#576ce6] grow min-h-px min-w-px relative rounded-[8px] shrink-0 cursor-pointer hover:bg-[#4759d1] transition-colors"
      data-name="Button"
    >
      <div className="flex flex-row items-center justify-center overflow-clip rounded-[inherit] size-full">
        <div className="content-stretch flex gap-[8px] items-center justify-center p-[12px] relative w-full">
          <p className="font-['Inter:Regular',sans-serif] font-normal leading-none not-italic relative shrink-0 text-[16px] text-neutral-100 text-nowrap whitespace-pre">Submit</p>
        </div>
      </div>
      <div aria-hidden="true" className="absolute border border-[#2c2c2c] border-solid inset-0 pointer-events-none rounded-[8px]" />
    </button>
  );
}

function Submit({ onClick }: { onClick: () => void }) {
  return (
    <div className="content-stretch flex gap-[16px] h-[27px] items-center relative shrink-0 w-[155px]" data-name="Submit">
      <Button onClick={onClick} />
    </div>
  );
}

function FormLogIn({ value, onChange, onSubmit }: { value: string; onChange: (value: string) => void; onSubmit: () => void }) {
  return (
    <div className="absolute bg-[#f5f8f9] content-stretch flex flex-col gap-[24px] h-[555px] items-start left-[242px] min-w-[320px] p-[24px] rounded-[8px] top-[199px] w-[956px]" data-name="Form Log In">
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-0 pointer-events-none rounded-[8px]" />
      <Description />
      <Q1Type value={value} onChange={onChange} />
      <Submit onClick={onSubmit} />
    </div>
  );
}

export default function FormPage({ onSubmit }: { onSubmit: () => void }) {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = () => {
    if (inputValue.trim()) {
      onSubmit();
    } else {
      alert('Please enter a description of what you are looking for in a club or organization');
    }
  };

  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec]" data-name="Form Page">
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      <FormLogIn value={inputValue} onChange={setInputValue} onSubmit={handleSubmit} />
    </div>
  );
}