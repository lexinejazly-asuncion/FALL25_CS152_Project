import { useState } from 'react';
import svgPaths from "../imports/svg-3otv47fjg0";

interface RSO {
  id: number;
  name: string;
  tags?: string;
}

interface RecommendationPageProps {
  rsos: RSO[];
  onSaveToProfile: (starredRSOs: RSO[]) => void;
}

function Star({ filled, onClick }: { filled: boolean; onClick: () => void }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className="size-[24px] cursor-pointer bg-transparent border-none p-0 hover:opacity-70 transition-opacity"
      data-name="star"
    >
      <svg className="block size-full" fill="none" preserveAspectRatio="none" viewBox="0 0 24 24">
        <g id="star">
          <path d={svgPaths.p3f7ca500} fill={filled ? "#FFD700" : "#1D1B20"} id="icon" />
        </g>
      </svg>
    </button>
  );
}

function SuggestionCard({ rso, starred, onToggleStar }: { rso: RSO; starred: boolean; onToggleStar: () => void }) {
  return (
    <div className="bg-[#f0f9fc] border border-[#757575] border-solid h-[60px] rounded-[5px] w-full px-4 flex items-center justify-between">
      <p className="font-['CantoraOne:Regular',sans-serif] leading-[30px] not-italic text-[#1e1e1e] text-[24px] tracking-[-0.48px]">
        {rso.name}
      </p>
      <Star filled={starred} onClick={onToggleStar} />
    </div>
  );
}

function Button({ onClick }: { onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="bg-[#576ce6] relative rounded-[8px] shrink-0 cursor-pointer hover:bg-[#4759d1] transition-colors"
      data-name="Button"
    >
      <div className="flex flex-row items-center justify-center overflow-clip rounded-[inherit] size-full">
        <div className="content-stretch flex gap-[8px] items-center justify-center p-[12px] relative w-full">
          <p className="font-['Inter:Regular',sans-serif] font-normal leading-none not-italic relative shrink-0 text-[16px] text-neutral-100 text-nowrap whitespace-pre">Go to Profile</p>
        </div>
      </div>
      <div aria-hidden="true" className="absolute border border-[#2c2c2c] border-solid inset-0 pointer-events-none rounded-[8px]" />
    </button>
  );
}

function Text() {
  return (
    <div className="content-stretch flex items-start relative shrink-0" data-name="Text">
      <div className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#757575] text-[16px] text-nowrap whitespace-pre">
        <p className="mb-0">Here are some recommended clubs and organizations based on your interests!</p>
        <p>Star the RSOs that you would like saved to your profile.</p>
      </div>
    </div>
  );
}

function Description() {
  return (
    <div className="content-stretch flex flex-col gap-[4px] items-start mb-6" data-name="Description">
      <p className="font-['Inter:Semi_Bold',sans-serif] font-semibold leading-[1.2] not-italic text-[#1e1e1e] text-[24px] tracking-[-0.48px]">FoundYourFit</p>
      <Text />
    </div>
  );
}

export default function RecommendationPage({ rsos, onSaveToProfile }: RecommendationPageProps) {
  const [starredIds, setStarredIds] = useState<Set<number>>(new Set());

  const toggleStar = (id: number) => {
    const newStarred = new Set(starredIds);
    if (newStarred.has(id)) {
      newStarred.delete(id);
    } else {
      newStarred.add(id);
    }
    setStarredIds(newStarred);
  };

  const handleGoToProfile = () => {
    const starred = rsos.filter(rso => starredIds.has(rso.id));
    if (starred.length === 0) {
      alert('Please star at least one RSO to save to your profile');
      return;
    }
    onSaveToProfile(starred);
  };

  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec] min-h-screen" data-name="Recommendation Page">
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      
      <div className="absolute bg-[#f5f8f9] border border-[#d9d9d9] border-solid left-[333px] rounded-[8px] top-[240px] w-[775px] p-[24px]">
        <Description />
        
        <div className="flex flex-col gap-4 mb-6 max-h-[380px] overflow-y-auto pr-2">
          {rsos.map((rso) => (
            <SuggestionCard
              key={rso.id}
              rso={rso}
              starred={starredIds.has(rso.id)}
              onToggleStar={() => toggleStar(rso.id)}
            />
          ))}
        </div>
        
        <Button onClick={handleGoToProfile} />
      </div>
    </div>
  );
}
