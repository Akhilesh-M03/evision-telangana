import { ArrowRight } from 'lucide-react';

export function CTAButton({ text = 'EXPLORE DASHBOARD', className = '', onClick }) {
  return (
    <button
      onClick={onClick}
      className={`
        inline-flex items-center gap-5 px-10 py-4.5 rounded-full
        bg-[#2a5c24] hover:bg-[#1e441a] text-white font-bold text-[14px] tracking-widest
        shadow-[0_4px_16px_rgba(42,92,36,0.3)]
        transition-all duration-200 cursor-pointer ${className}
      `}
    >
      <span>{text}</span>
      <ArrowRight className="w-5 h-5 text-white" strokeWidth={2} />
    </button>
  );
}
