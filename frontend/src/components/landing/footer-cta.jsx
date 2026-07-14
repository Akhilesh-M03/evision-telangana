import { Leaf } from 'lucide-react';

export function FooterCTA() {
  return (
    <section className="relative w-full py-8 lg:py-10 bg-gradient-to-t from-[#388e3c]/25 via-[#81c784]/10 to-transparent overflow-hidden border-t border-gray-100">
      <div className="absolute inset-0 opacity-[0.08]">
        <svg viewBox="0 0 1000 400" className="w-full h-full">
          <g transform="translate(50, 310)">
            <rect x="0" y="0" width="30" height="30" fill="none" stroke="#666" strokeWidth="1" />
            <line x1="15" y1="0" x2="15" y2="30" stroke="#666" strokeWidth="0.5" />
            <line x1="0" y1="15" x2="30" y2="15" stroke="#666" strokeWidth="0.5" />
            <rect x="35" y="0" width="30" height="30" fill="none" stroke="#666" strokeWidth="1" />
            <line x1="50" y1="0" x2="50" y2="30" stroke="#666" strokeWidth="0.5" />
            <line x1="35" y1="15" x2="65" y2="15" stroke="#666" strokeWidth="0.5" />
          </g>
          <g transform="translate(150, 310)">
            <circle cx="0" cy="0" r="15" fill="none" stroke="#999" strokeWidth="1" />
            <line x1="0" y1="0" x2="0" y2="25" stroke="#999" strokeWidth="1" />
          </g>
          <rect x="250" y="290" width="50" height="80" fill="none" stroke="#999" strokeWidth="1" />
          <line x1="275" y1="290" x2="275" y2="370" stroke="#999" strokeWidth="0.5" />
          <g transform="translate(400, 260)">
            <line x1="0" y1="0" x2="0" y2="80" stroke="#ccc" strokeWidth="1" />
            <circle cx="0" cy="-10" r="3" fill="#ccc" />
            <path d="M 0 -10 L 8 -20 L 6 -15 Z" fill="#ddd" />
            <path d="M 0 -10 L 8 -20 L 6 -15 Z" fill="#ddd" transform="rotate(120)" />
            <path d="M 0 -10 L 8 -20 L 6 -15 Z" fill="#ddd" transform="rotate(240)" />
          </g>
          <g transform="translate(600, 320)">
            <circle cx="0" cy="0" r="20" fill="none" stroke="#aaa" strokeWidth="1" />
            <line x1="0" y1="0" x2="0" y2="20" stroke="#aaa" strokeWidth="1" />
          </g>
          <circle cx="750" cy="330" r="12" fill="none" stroke="#bbb" strokeWidth="0.5" />
          <circle cx="800" cy="340" r="10" fill="none" stroke="#bbb" strokeWidth="0.5" />
          <circle cx="850" cy="335" r="15" fill="none" stroke="#bbb" strokeWidth="0.5" />
          <circle cx="920" cy="345" r="12" fill="none" stroke="#bbb" strokeWidth="0.5" />
        </svg>
      </div>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center flex flex-col items-center justify-center gap-2">
        <div className="flex justify-center">
          <Leaf className="w-7 h-7 text-[#2e7d32] fill-green-100" />
        </div>

        <h2 className="text-xl md:text-2xl font-bold leading-tight text-gray-900">
          Let&apos;s Build a Smarter,{' '}
          <span className="bg-gradient-to-r from-[#388e3c] to-[#81c784] bg-clip-text text-transparent font-extrabold">
            Greener Telangana.
          </span>
        </h2>

        <p className="text-xs text-gray-500 max-w-2xl mx-auto font-semibold">
          Smarter infrastructure today for a sustainable tomorrow.
        </p>
      </div>
    </section>
  );
}
