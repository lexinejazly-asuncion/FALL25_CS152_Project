interface RSO {
  id: number;
  name: string;
  tags?: string;
}

interface ProfilePageProps {
  savedRSOs: RSO[];
  onRecommendMeClubs: () => void;
  onLogout: () => void;
}

function SuggestionCard({ rso }: { rso: RSO }) {
  return (
    <div className="bg-[#f0f9fc] border border-[#757575] border-solid h-[59px] rounded-[5px] w-full px-4 flex items-center">
      <p className="font-['CantoraOne:Regular',sans-serif] leading-[30px] not-italic text-[#1e1e1e] text-[24px] tracking-[-0.48px]">
        {rso.name}
      </p>
    </div>
  );
}

function Text() {
  return (
    <div className="content-stretch flex items-start relative shrink-0" data-name="Text">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#757575] text-[16px] text-nowrap whitespace-pre">Here is a list of your recommended and saved clubs and organizations</p>
    </div>
  );
}

function Description() {
  return (
    <div className="content-stretch flex flex-col gap-[4px] items-start mb-6" data-name="Description">
      <p className="font-['Inter:Semi_Bold',sans-serif] font-semibold leading-[1.2] not-italic text-[#1e1e1e] text-[24px] tracking-[-0.48px]">FoundYourRSOs</p>
      <Text />
    </div>
  );
}

function RecommendButton({ onClick }: { onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="bg-[#576ce6] relative rounded-[8px] cursor-pointer hover:bg-[#4759d1] transition-colors px-6 py-3"
    >
      <div className="flex items-center justify-center">
        <p className="font-['Inter:Regular',sans-serif] font-normal leading-none not-italic text-[16px] text-neutral-100 text-nowrap whitespace-pre">Recommend Me Clubs</p>
      </div>
      <div aria-hidden="true" className="absolute border border-[#2c2c2c] border-solid inset-0 pointer-events-none rounded-[8px]" />
    </button>
  );
}

export default function ProfilePage({ savedRSOs, onRecommendMeClubs, onLogout }: ProfilePageProps) {
  const hasRSOs = savedRSOs.length > 0;

  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec] min-h-screen" data-name="Profile">
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      
      <button
        onClick={onLogout}
        className="absolute right-[100px] top-[100px] font-['Inter:Regular',sans-serif] font-normal text-[16px] text-black underline cursor-pointer hover:text-[#576ce6] transition-colors bg-transparent border-none"
      >
        Log Out
      </button>
      
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-141px)] text-[48px] text-black text-nowrap top-[164px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        Hello, Name!
      </p>
      
      <div className="absolute bg-[#f5f8f9] border border-[#d9d9d9] border-solid left-[372px] rounded-[8px] top-[287px] w-[696px] p-[24px]">
        {hasRSOs ? (
          <>
            <Description />
            <div className="flex flex-col gap-4 mb-6 max-h-[350px] overflow-y-auto pr-2">
              {savedRSOs.map((rso) => (
                <SuggestionCard key={rso.id} rso={rso} />
              ))}
            </div>
            <RecommendButton onClick={onRecommendMeClubs} />
          </>
        ) : (
          <div className="flex flex-col items-center justify-center py-12">
            <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic text-[#757575] text-[16px] mb-6 text-center">
              You don&apos;t have any saved RSOs yet.
              <br />
              Get personalized recommendations to find your perfect fit!
            </p>
            <RecommendButton onClick={onRecommendMeClubs} />
          </div>
        )}
      </div>
    </div>
  );
}