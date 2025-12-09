import { useState } from 'react';
import svgPaths from "../imports/svg-x0naout6nh";

interface RSO {
  id: number;
  name: string;
  tags: string;
}

interface ExplorePageProps {
  onSubmit: (selectedRSOs: RSO[]) => void;
}

// Mock RSO data
const MOCK_RSOS: RSO[] = [
  { id: 1, name: 'Computer Science Club', tags: 'Technology, Programming, Networking' },
  { id: 2, name: 'Photography Society', tags: 'Arts, Photography, Creative' },
  { id: 3, name: 'Debate Team', tags: 'Communication, Leadership, Public Speaking' },
  { id: 4, name: 'Environmental Action Group', tags: 'Sustainability, Community, Activism' },
  { id: 5, name: 'Dance Ensemble', tags: 'Arts, Performance, Fitness' },
  { id: 6, name: 'Entrepreneurship Club', tags: 'Business, Innovation, Networking' },
];

function CheckBox({ checked, onChange }: { checked: boolean; onChange: () => void }) {
  return (
    <button
      type="button"
      onClick={onChange}
      className="size-[24px] cursor-pointer bg-transparent border-none p-0"
      data-name="check_box"
    >
      <svg className="block size-full" fill="none" preserveAspectRatio="none" viewBox="0 0 24 24">
        <g id="check_box">
          <path d={svgPaths.p29256980} fill={checked ? "#576ce6" : "#1D1B20"} id="icon" />
        </g>
      </svg>
    </button>
  );
}

function SuggestionCard({ rso, checked, onChange }: { rso: RSO; checked: boolean; onChange: () => void }) {
  return (
    <div className="bg-[#f0f9fc] border border-[#757575] border-solid h-[88px] rounded-[5px] w-full p-4 flex items-center justify-between">
      <div className="flex-1">
        <p className="font-['CantoraOne:Regular',sans-serif] leading-[30px] not-italic text-[#1e1e1e] text-[24px] tracking-[-0.48px] mb-0">
          {rso.name}
        </p>
        <p className="font-['CantoraOne:Regular',sans-serif] leading-[30px] not-italic text-[#1e1e1e] text-[16px] tracking-[-0.48px] mb-0">
          Tags: {rso.tags}
        </p>
      </div>
      <CheckBox checked={checked} onChange={onChange} />
    </div>
  );
}

function Text() {
  return (
    <div className="content-stretch flex items-start relative shrink-0" data-name="Text">
      <p className="font-['Inter:Regular',sans-serif] font-normal leading-[1.4] not-italic relative shrink-0 text-[#757575] text-[16px] text-nowrap whitespace-pre">Explore and select clubs or organizations that you like</p>
    </div>
  );
}

function Description() {
  return (
    <div className="content-stretch flex flex-col gap-[4px] items-start mb-6" data-name="Description">
      <p className="font-['Inter:Semi_Bold',sans-serif] font-semibold leading-[1.2] not-italic text-[#1e1e1e] text-[24px] tracking-[-0.48px]">FindYourFit</p>
      <Text />
    </div>
  );
}

function Button({ onClick }: { onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      className="bg-[#576ce6] relative rounded-[8px] cursor-pointer hover:bg-[#4759d1] transition-colors"
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

export default function ExplorePage({ onSubmit }: ExplorePageProps) {
  const [selectedIds, setSelectedIds] = useState<Set<number>>(new Set());

  const toggleSelection = (id: number) => {
    const newSelected = new Set(selectedIds);
    if (newSelected.has(id)) {
      newSelected.delete(id);
    } else {
      newSelected.add(id);
    }
    setSelectedIds(newSelected);
  };

  const handleSubmit = () => {
    const selected = MOCK_RSOS.filter(rso => selectedIds.has(rso.id));
    if (selected.length === 0) {
      alert('Please select at least one RSO');
      return;
    }
    onSubmit(selected);
  };

  return (
    <div className="bg-gradient-to-b from-[#b2cff3] relative size-full to-[#b2bbec] min-h-screen" data-name="Explore Page">
      <p className="absolute font-['Bricolage_Grotesque:Bold',sans-serif] font-bold leading-[84px] left-[calc(50%-618px)] text-[#576ce6] text-[48px] text-nowrap top-[80px] tracking-[-0.96px] whitespace-pre" style={{ fontVariationSettings: "'opsz' 14, 'wdth' 100" }}>
        FindYourRSO
      </p>
      
      <div className="absolute bg-[#f5f8f9] border border-[#d9d9d9] border-solid left-[242px] rounded-[8px] top-[264px] w-[956px] p-[24px]">
        <Description />
        
        <div className="grid grid-cols-2 gap-4 mb-6 max-h-[400px] overflow-y-auto pr-2">
          {MOCK_RSOS.map((rso) => (
            <SuggestionCard
              key={rso.id}
              rso={rso}
              checked={selectedIds.has(rso.id)}
              onChange={() => toggleSelection(rso.id)}
            />
          ))}
        </div>
        
        <Button onClick={handleSubmit} />
      </div>
    </div>
  );
}
