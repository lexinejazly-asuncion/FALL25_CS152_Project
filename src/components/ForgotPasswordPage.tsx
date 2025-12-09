import { useState } from 'react';

interface ForgotPasswordPageProps {
  onBack: () => void;
}

function Input({ type, value, onChange, placeholder }: { type: string; value: string; onChange: (value: string) => void; placeholder: string }) {
  return (
    <div className="bg-white min-w-[240px] relative rounded-[8px] shrink-0 w-full" data-name="Input">
      <div className="flex flex-row items-center min-w-[inherit] overflow-clip rounded-[inherit] size-full">
        <div className="content-stretch flex items-center min-w-[inherit] px-[16px] py-[12px] relative w-full">
          <input
            type={type}
            value={value}
            onChange={(e) => onChange(e.target.value)}
            placeholder={placeholder}
            className="basis-0 font-['Inter:Regular',sans-serif] font-normal grow leading-none min-h-px min-w-px not-italic relative shrink-0 text-[#1e1e1e] text-[16px] placeholder:text-[#b3b3b3] bg-transparent border-none outline-none w-full"
          />
        </div>
      </div>
      <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-[-0.5px] pointer-events-none rounded-[8.5px]" />
    </div>
  );
}

function InputField({ label, type, value, onChange, placeholder }: { label: string; type: string; value: string; onChange: (value: string) => void; placeholder: string }) {
  return (
    <div className="content-stretch flex flex-col gap-[8px] items-start relative shrink-0 w-full" data-name="Input Field">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] min-w-full not-italic relative shrink-0 text-[#1e1e1e] text-[16px] w-[min-content]">{label}</p>
      <Input type={type} value={value} onChange={onChange} placeholder={placeholder} />
    </div>
  );
}

export default function ForgotPasswordPage({ onBack }: ForgotPasswordPageProps) {
  const [email, setEmail] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle password reset
    alert('Password reset link sent to your email!');
    onBack();
  };

  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec]">
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-237px)] text-[48px] text-black text-nowrap top-[280px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        Reset Password
      </p>
      
      <form
        onSubmit={handleSubmit}
        className="absolute bg-[#f5f8f9] content-stretch flex flex-col gap-[24px] items-start left-[483px] min-w-[320px] p-[24px] rounded-[8px] top-[406px] w-[480px]"
      >
        <div aria-hidden="true" className="absolute border border-[#d9d9d9] border-solid inset-0 pointer-events-none rounded-[8px]" />
        
        <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic text-[#1e1e1e] text-[16px]">
          Enter your email address and we&apos;ll send you a link to reset your password.
        </p>
        
        <InputField label="Email" type="email" value={email} onChange={setEmail} placeholder="Enter your email" />
        
        <button
          type="submit"
          className="basis-0 bg-[#576ce6] grow min-h-px min-w-px relative rounded-[8px] shrink-0 cursor-pointer hover:bg-[#4759d1] transition-colors w-full"
        >
          <div className="flex flex-row items-center justify-center overflow-clip rounded-[inherit] size-full">
            <div className="content-stretch flex gap-[8px] items-center justify-center p-[12px] relative w-full">
              <p className="font-['Inter:Regular',sans-serif] font-normal leading-none not-italic relative shrink-0 text-[16px] text-neutral-100 text-nowrap whitespace-pre">Send Reset Link</p>
            </div>
          </div>
          <div aria-hidden="true" className="absolute border border-[#2c2c2c] border-solid inset-0 pointer-events-none rounded-[8px]" />
        </button>

        <button
          type="button"
          onClick={onBack}
          className="[text-decoration-skip-ink:none] [text-underline-position:from-font] decoration-solid font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#1e1e1e] text-[16px] text-nowrap underline whitespace-pre cursor-pointer hover:text-[#576ce6] transition-colors bg-transparent border-none"
        >
          Back to Sign In
        </button>
      </form>
    </div>
  );
}