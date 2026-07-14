import {
  Cpu,
  GitCompare,
  History,
  IndianRupee,
  Leaf,
  LineChart,
  ListOrdered,
  Clock,
  MapPin,
  MessageSquare,
  Sparkles,
} from 'lucide-react';
import { CTAButton } from './cta-button';

const plannerFeatures = [
  {
    icon: MapPin,
    title: 'Interactive Telangana GIS Map',
    description: 'Explore charging stations, grid capacity, and demand hotspots across the state.',
  },
  {
    icon: LineChart,
    title: 'Live Analytics Dashboard',
    description: 'Real-time metrics on charger utilization, energy load, and district progress.',
  },
  {
    icon: Sparkles,
    title: 'Future EV Demand Prediction',
    description: 'AI-driven forecasting models to predict EV growth and charging demand.',
  },
  {
    icon: ListOrdered,
    title: 'District Priority Ranking',
    description: 'Identify top districts for investment and expansion using composite scores.',
  },
  {
    icon: Cpu,
    title: 'Explainable AI Decision Support',
    description: 'Understand the key factors behind AI location recommendations.',
  },
  {
    icon: History,
    title: 'Historical Trend Analysis',
    description: 'Analyze past patterns of EV adoption and charger deployment over time.',
  },
  {
    icon: GitCompare,
    title: 'District Comparison & Insights',
    description: 'Compare districts side-by-side on key metrics to discover insights.',
  },
  {
    icon: MessageSquare,
    title: 'AI Planning Assistant',
    description: 'Conversational assistant to answer infrastructure queries and guide planning decisions.',
  },
];

export function HeroSection({ onExploreDashboard }) {
  return (
    <section className="relative w-full overflow-hidden bg-white flex flex-col">
      <div className="absolute right-0 top-0 h-screen w-[55vw] bg-[url('/hero_background.png')] bg-cover bg-[center_top] bg-no-repeat pointer-events-none z-0">
        <div className="absolute inset-y-0 left-0 w-[200px] lg:w-[350px] bg-gradient-to-r from-white via-white/80 to-transparent z-10" />
      </div>

      <div className="max-w-7xl mx-auto px-6 lg:px-12 relative z-10 w-full min-h-screen flex items-center pt-24 pb-12">
        <div className="grid grid-cols-1 lg:grid-cols-[40%_60%] gap-6 items-center w-full">
          <div className="flex flex-col gap-8 pt-32 pb-12 lg:py-0 lg:-mt-40">
            <div className="flex flex-col gap-2">
              <h2 className="text-4xl sm:text-5xl lg:text-[68px] xl:text-[72px] font-bold leading-[1.1] tracking-tight text-[#0f172a] sm:whitespace-nowrap">
                Smarter Planning.
              </h2>
              <h2 className="text-4xl sm:text-5xl lg:text-[68px] xl:text-[72px] font-bold leading-[1.1] tracking-tight text-[#2d6a31] sm:whitespace-nowrap">
                Sustainable Future.
              </h2>
            </div>

            <p className="text-[16px] lg:text-[18px] text-[#475569] leading-relaxed max-w-[540px]">
              EVision Telangana uses AI and real-time data to plan the right EV infrastructure, at the right places
              for a cleaner, greener and future-ready Telangana.
            </p>

            <div className="pt-2">
              <CTAButton onClick={onExploreDashboard} />
            </div>
          </div>

          <div className="relative flex items-end justify-center lg:justify-end h-[500px] lg:h-[750px] xl:h-[840px] w-full z-20 lg:-mt-28">
            <img
              src="/ev_car.png"
              alt="EV car at charging station"
              className="absolute inset-0 h-full w-full object-contain object-bottom lg:object-right-bottom scale-115 lg:scale-145 xl:scale-155 origin-bottom lg:-translate-x-8 xl:-translate-x-12"
            />
          </div>
        </div>
      </div>

      <div className="w-full relative z-30 pb-0 pt-16 bg-white">
        <div className="max-w-7xl mx-auto px-6 lg:px-12">
          <div className="w-full border border-gray-100 rounded-3xl bg-white p-8 lg:p-10 grid grid-cols-1 lg:grid-cols-[55%_45%] gap-8 lg:gap-12 shadow-[0_4px_30px_rgba(0,0,0,0.02)] mb-20">
            <div className="flex flex-col gap-10 lg:border-r lg:border-gray-100 lg:pr-10">
              <div className="flex items-start gap-6">
                <div className="w-16 h-16 rounded-full bg-green-50 flex items-center justify-center text-[#2a5c24] flex-shrink-0 shadow-inner">
                  <Leaf className="w-8 h-8 fill-green-200" />
                </div>
                <div className="flex flex-col gap-2">
                  <h3 className="text-lg lg:text-xl font-bold text-[#1b5e20]">What is EVision Telangana?</h3>
                  <p className="text-sm text-gray-500 leading-relaxed">
                    EVision Telangana is an AI-powered platform that helps plan and scale EV charging infrastructure.
                    We optimize charger placement by analyzing traffic patterns, power grid capacity, and driver
                    density to enable a seamless transition to green mobility.
                  </p>
                </div>
              </div>

              <div className="w-full h-px bg-gray-100" />

              <div className="flex flex-col gap-4">
                <h3 className="text-lg lg:text-xl font-bold text-[#1b5e20]">Why EVision Telangana?</h3>
                <div className="grid grid-cols-2 gap-4">
                  <div className="flex items-start gap-3">
                    <IndianRupee className="w-5 h-5 text-[#2e7d32] mt-0.5 flex-shrink-0" />
                    <div>
                      <h4 className="text-xs font-bold text-gray-800">Optimize Costs</h4>
                      <p className="text-[11px] text-gray-500 leading-tight">Reduce waste with high-yield locations.</p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <Clock className="w-5 h-5 text-[#2e7d32] mt-0.5 flex-shrink-0" />
                    <div>
                      <h4 className="text-xs font-bold text-gray-800">Save Time</h4>
                      <p className="text-[11px] text-gray-500 leading-tight">
                        Deploy chargers faster with ready grid data.
                      </p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <Sparkles className="w-5 h-5 text-[#2e7d32] mt-0.5 flex-shrink-0" />
                    <div>
                      <h4 className="text-xs font-bold text-gray-800">Live Smarter</h4>
                      <p className="text-[11px] text-gray-500 leading-tight">
                        Use predictive AI models for placement.
                      </p>
                    </div>
                  </div>

                  <div className="flex items-start gap-3">
                    <Leaf className="w-5 h-5 text-[#2e7d32] mt-0.5 flex-shrink-0" />
                    <div>
                      <h4 className="text-xs font-bold text-gray-800">Save Earth</h4>
                      <p className="text-[11px] text-gray-500 leading-tight">Accelerate CO2 offset in the state.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div className="relative w-full h-[320px] lg:h-auto min-h-[300px] lg:min-h-[400px] rounded-2xl overflow-hidden shadow-inner bg-white border border-gray-100 flex items-center justify-center">
              <img
                src="/card_ev_map.png"
                alt="EV Charging Network Planner Map"
                className="absolute inset-0 h-full w-full object-contain p-4"
              />
            </div>
          </div>

          <div className="text-center mb-12">
            <h3 className="text-2xl lg:text-3xl font-bold text-gray-900">
              <span className="text-[#1b5e20]">Features</span> You&apos;ll Love
            </h3>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 mb-16">
            {plannerFeatures.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <div
                  key={index}
                  className="flex flex-col sm:flex-row items-start gap-4 p-5 rounded-2xl bg-white border border-gray-100 shadow-[0_4px_20px_rgba(0,0,0,0.02)] hover:shadow-[0_8px_30px_rgba(0,0,0,0.06)] hover:-translate-y-1 transition-all duration-300"
                >
                  <div className="w-12 h-12 rounded-2xl bg-[#2a5c24] flex items-center justify-center text-white flex-shrink-0 shadow-md shadow-green-900/10">
                    <Icon className="w-5 h-5" strokeWidth={2} />
                  </div>

                  <div className="flex flex-col gap-1">
                    <h4 className="text-sm font-bold text-gray-900 leading-snug">{feature.title}</h4>
                    <p className="text-xs text-gray-500 leading-relaxed">{feature.description}</p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}
