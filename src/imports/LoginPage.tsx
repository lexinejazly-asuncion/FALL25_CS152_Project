function Input() {
  return (
    <div className="bg-white min-w-[240px] relative rounded-[8px] shrink-0 w-full" data-name="Input">
      <div className="flex flex-row items-center min-w-[inherit] overflow-clip rounded-[inherit] size-full">
        <div className="content-stretch flex items-center min-w-[inherit] px-[16px] py-[12px] relative w-full">
          <p className="basis-0 font-['Inter:Regular',sans-serif] font-normal grow leading-none min-h-px min-w-px not-italic relative shrink-0 text-[#b3b3b3] text-[16px]">Value</p>
        </div>
      </div>
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-[-0.5px] pointer-events-none rounded-[8.5px]" />
    </div>
  );
}

function InputField() {
  return (
    <div className="content-stretch flex flex-col gap-[8px] items-start relative shrink-0 w-full" data-name="Input Field">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] min-w-full not-italic relative shrink-0 text-[#1e1e1e] text-[16px] w-[min-content]">Email</p>
      <Input />
    </div>
  );
}

function Input1() {
  return (
    <div className="bg-white min-w-[240px] relative rounded-[8px] shrink-0 w-full" data-name="Input">
      <div className="flex flex-row items-center min-w-[inherit] overflow-clip rounded-[inherit] size-full">
        <div className="content-stretch flex items-center min-w-[inherit] px-[16px] py-[12px] relative w-full">
          <p className="basis-0 font-['Inter:Regular',sans-serif] font-normal grow leading-none min-h-px min-w-px not-italic relative shrink-0 text-[#b3b3b3] text-[16px]">Value</p>
        </div>
      </div>
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-[-0.5px] pointer-events-none rounded-[8.5px]" />
    </div>
  );
}

function InputField1() {
  return (
    <div className="content-stretch flex flex-col gap-[8px] items-start relative shrink-0 w-full" data-name="Input Field">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] min-w-full not-italic relative shrink-0 text-[#1e1e1e] text-[16px] w-[min-content]">Password</p>
      <Input1 />
    </div>
  );
}

function Button() {
  return (
    <div className="basis-0 bg-[#576ce6] grow min-h-px min-w-px relative rounded-[8px] shrink-0" data-name="Button">
      <div className="flex flex-row items-center justify-center overflow-clip rounded-[inherit] size-full">
        <div className="content-stretch flex gap-[8px] items-center justify-center p-[12px] relative w-full">
          <p className="font-['Inter:Regular',sans-serif] font-normal leading-none not-italic relative shrink-0 text-[16px] text-neutral-100 text-nowrap whitespace-pre">Sign In</p>
        </div>
      </div>
      <div aria-hidden="true" className="absolute border border-[#2c2c2c] border-solid inset-0 pointer-events-none rounded-[8px]" />
    </div>
  );
}

function ButtonGroup() {
  return (
    <div className="content-stretch flex gap-[16px] items-center relative shrink-0 w-full" data-name="Button Group">
      <Button />
    </div>
  );
}

function TextLink() {
  return (
    <div className="content-stretch flex items-start relative shrink-0 w-full" data-name="Text Link">
      <p className="[text-decoration-skip-ink:none] [text-underline-position:from-font] decoration-solid font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#1e1e1e] text-[16px] text-nowrap underline whitespace-pre">Forgot password?</p>
    </div>
  );
}

function FormLogIn() {
  return (
    <div className="absolute bg-[#f5f8f9] content-stretch flex flex-col gap-[24px] h-[341px] items-start left-[483px] min-w-[320px] p-[24px] rounded-[8px] top-[406px] w-[480px]" data-name="Form Log In">
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-0 pointer-events-none rounded-[8px]" />
      <InputField />
      <InputField1 />
      <ButtonGroup />
      <TextLink />
    </div>
  );
}

export default function LoginPage() {
  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec]" data-name="Login Page">
      <FormLogIn />
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-237px)] text-[48px] text-black text-nowrap top-[280px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        Sign in
      </p>
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-237px)] text-[20px] text-black text-nowrap top-[322px] tracking-[-0.4px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        or create an account
      </p>
    </div>
  );
}