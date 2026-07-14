import { FooterCTA } from './footer-cta';
import { Header } from './header';
import { HeroSection } from './hero-section';

export function EVisionTelanganaLanding({ onExploreDashboard }) {
  return (
    <main className="w-full min-h-screen bg-white text-foreground overflow-x-hidden">
      <Header />
      <HeroSection onExploreDashboard={onExploreDashboard} />
      <FooterCTA />
    </main>
  );
}
