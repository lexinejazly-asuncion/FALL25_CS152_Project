interface LandingPageProps {
  onGetStarted: () => void;
}

function Button({ onClick }: { onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="absolute bg-[#576ce6] h-[63px] left-[570px] rounded-[8px] top-[630px] w-[299px] cursor-pointer hover:bg-[#4759d1] transition-colors"
      data-name="Button"
    >
      <div className="content-stretch flex gap-[8px] h-[63px] items-center justify-center overflow-clip p-[12px] relative rounded-[inherit] w-[299px]">
        <p className="font-['Inter:Regular',sans-serif] font-normal leading-none not-italic relative shrink-0 text-[16px] text-nowrap text-white whitespace-pre">Get Started!</p>
      </div>
      <div aria-hidden="true" className="absolute border border-[#2c2c2c] border-solid inset-0 pointer-events-none rounded-[8px]" />
    </button>
  );
}

export default function LandingPage({ onGetStarted }: LandingPageProps) {
  return (
    <div className="bg-gradient-to-b from-[#b2bbec] relative size-full to-[#b2cff3]" data-name="Landing Page">
      <Button onClick={onGetStarted} />
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-534px)] text-[#576ce6] text-[96px] text-nowrap top-[178px] tracking-[-1.92px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-534px)] text-[48px] text-black text-nowrap top-[325px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FOMO? Never heard of it.
      </p>
      <p className="absolute font-['Carrois_Gothic:Regular',sans-serif] h-[167px] leading-[25px] left-[calc(50%-534px)] not-italic text-[24px] text-black top-[429px] tracking-[-0.48px] w-[1069px]">
        {`Discover clubs and organizations that match your interests, schedule, and goals all in one place. `}
        <br aria-hidden="true" />
        <br aria-hidden="true" />
        FindYourRSO connects San José State University students with RSOs that align with who they are and what they love. No more hoping to stumble across the right club or missing campus events, just personalized recommendations that help you get involved and find your community.
      </p>
    </div>
  );
}
