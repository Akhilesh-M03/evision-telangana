import { Zap } from 'lucide-react';

export function Header() {
  return (
    <header className="absolute top-0 left-0 right-0 z-50 bg-transparent">
      <div className="max-w-7xl mx-auto px-6 lg:px-12 pt-8 pb-4 flex items-center gap-3">
        <div className="flex items-center gap-3.5">
          <div className="w-12 h-12 bg-[#1b5e20] rounded-full flex items-center justify-center">
            <Zap className="w-7 h-7 text-white fill-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 leading-tight">
              <span className="text-[#1b5e20]">EVision</span> Telangana
            </h1>
            <p className="text-xs lg:text-sm font-medium text-gray-500 mt-0.5">
              AI-Powered EV Infrastructure Planner
            </p>
          </div>
        </div>
      </div>
    </header>
  );
}
