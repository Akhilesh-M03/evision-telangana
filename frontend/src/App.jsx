import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Zap, 
  ArrowRight, 
  TrendingUp, 
  Target, 
  Bot, 
  MapPin, 
  LineChart as ChartIcon, 
  Layers, 
  MessageSquare, 
  ArrowLeft, 
  Send, 
  Activity, 
  ShieldCheck,
  Compass
} from 'lucide-react';
import { MapContainer, TileLayer, CircleMarker, Popup, useMap } from 'react-leaflet';
import { 
  ResponsiveContainer, 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend 
} from 'recharts';

import 'leaflet/dist/leaflet.css';
import figCleanBoth from './assets/fig_clean_both.png';

// Realistic mock data for Telangana districts
const districtData = {
  "Hyderabad": {
    name: "Hyderabad",
    coordinates: [17.3850, 78.4867],
    priorityScore: 9.8,
    evCount: 24500,
    demand2026: 45,
    demand2028: 82,
    demand2030: 120,
    recs: [
      { type: "DC Ultra-Fast (150kW)", count: 45, area: "IT Corridors, Malls" },
      { type: "DC Fast (50kW)", count: 105, area: "Metro Stations, Commercial Hubs" },
      { type: "AC Type 2 (22kW)", count: 300, area: "Residential Societies, Office Parks" }
    ],
    details: "Critical priority due to high density of electric two-wheelers and passenger vehicles. Focus placement near high-traffic IT parks (Gachibowli, Hitec City) and major commercial centers.",
    feasibility: "94%"
  },
  "Rangareddy": {
    name: "Rangareddy",
    coordinates: [17.1812, 78.4328],
    priorityScore: 9.2,
    evCount: 18200,
    demand2026: 35,
    demand2028: 68,
    demand2030: 95,
    recs: [
      { type: "DC Ultra-Fast (150kW)", count: 30, area: "Outer Ring Road (ORR) Plazas" },
      { type: "DC Fast (50kW)", count: 80, area: "Transit Hubs, Highway Nodes" },
      { type: "AC Type 2 (22kW)", count: 220, area: "Tech Parks, Gated Communities" }
    ],
    details: "Very high priority. High demand growth along transit corridors and peripheral highways. Highly suitable for solar-powered highway charging stations.",
    feasibility: "89%"
  },
  "Medchal-Malkajgiri": {
    name: "Medchal-Malkajgiri",
    coordinates: [17.5449, 78.5718],
    priorityScore: 8.5,
    evCount: 12800,
    demand2026: 25,
    demand2028: 50,
    demand2030: 75,
    recs: [
      { type: "DC Ultra-Fast (150kW)", count: 20, area: "Industrial Clusters, Highway Exits" },
      { type: "DC Fast (50kW)", count: 60, area: "Suburban Centers, Junctions" },
      { type: "AC Type 2 (22kW)", count: 150, area: "Public Parking Lots, Shopping Complexes" }
    ],
    details: "High priority. Strong demand from industrial zones and residential commuters travelling into Hyderabad. Focus on heavy vehicle/delivery EV chargers.",
    feasibility: "86%"
  },
  "Warangal": {
    name: "Warangal",
    coordinates: [17.9784, 79.5941],
    priorityScore: 7.5,
    evCount: 4500,
    demand2026: 12,
    demand2028: 24,
    demand2030: 42,
    recs: [
      { type: "DC Fast (50kW)", count: 15, area: "Tourist Sites, Railway Station" },
      { type: "AC Type 2 (22kW)", count: 40, area: "University Campus, City Center" }
    ],
    details: "Medium-high priority. Key urban hub in East Telangana. High potential for public charging network linking to highway networks.",
    feasibility: "81%"
  },
  "Karimnagar": {
    name: "Karimnagar",
    coordinates: [18.4386, 79.1288],
    priorityScore: 7.0,
    evCount: 3800,
    demand2026: 8,
    demand2028: 18,
    demand2030: 30,
    recs: [
      { type: "DC Fast (50kW)", count: 12, area: "Karimnagar Bus Station, Bypass Road" },
      { type: "AC Type 2 (22kW)", count: 35, area: "Residential Layouts, Municipal Parkings" }
    ],
    details: "Medium priority. Focus on public transit electrification (e-buses and e-rickshaws) and connecting corridors to Hyderabad.",
    feasibility: "80%"
  },
  "Nizamabad": {
    name: "Nizamabad",
    coordinates: [18.6725, 78.0941],
    priorityScore: 6.5,
    evCount: 2900,
    demand2026: 6,
    demand2028: 13,
    demand2030: 20,
    recs: [
      { type: "DC Fast (50kW)", count: 8, area: "NH-44 Corridor, City Bypass" },
      { type: "AC Type 2 (22kW)", count: 28, area: "Distributor Points, Main Bazaar" }
    ],
    details: "Medium priority. High agricultural trade hub. Electrification of light commercial vehicles is key here.",
    feasibility: "74%"
  },
  "Nalgonda": {
    name: "Nalgonda",
    coordinates: [17.0575, 79.2684],
    priorityScore: 6.8,
    evCount: 2800,
    demand2026: 6,
    demand2028: 14,
    demand2030: 22,
    recs: [
      { type: "DC Fast (50kW)", count: 10, area: "Hyderabad-Vijayawada Highway (NH-65)" },
      { type: "AC Type 2 (22kW)", count: 25, area: "Local Bus Stands, Public Offices" }
    ],
    details: "Medium priority. Heavily reliant on highway transit corridor demand. Highly strategic for fast chargers on NH-65.",
    feasibility: "78%"
  },
  "Khammam": {
    name: "Khammam",
    coordinates: [17.2473, 80.1514],
    priorityScore: 6.2,
    evCount: 3100,
    demand2026: 5,
    demand2028: 12,
    demand2030: 18,
    recs: [
      { type: "DC Fast (50kW)", count: 8, area: "Town Entrance, Main Market" },
      { type: "AC Type 2 (22kW)", count: 30, area: "District Hospital, Shopping Streets" }
    ],
    details: "Medium-low priority. Growing commercial center. Steady demand for private two-wheelers and three-wheelers.",
    feasibility: "75%"
  }
};

// Component to dynamically pan Leaflet Map
function ChangeView({ center }) {
  const map = useMap();
  useEffect(() => {
    if (center) {
      map.setView(center, map.getZoom(), { animate: true, duration: 0.8 });
    }
  }, [center, map]);
  return null;
}

function App() {
  const [view, setView] = useState('landing'); // 'landing' or 'dashboard'
  const [dbTab, setDbTab] = useState('overview'); // 'overview', 'forecasting', 'recommendations', 'chatbot'
  const [selectedDistrict, setSelectedDistrict] = useState('Hyderabad');
  
  // Chat state
  const [chatHistory, setChatHistory] = useState([
    {
      sender: 'bot',
      text: "Hello! I'm your AI Decision Assistant. How can I help you plan EV infrastructure for Telangana today?"
    }
  ]);
  const [chatInput, setChatInput] = useState('');
  const chatEndRef = useRef(null);

  // Auto-scroll chat history
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatHistory]);

  const activeData = districtData[selectedDistrict];

  // Map markers list
  const districtsList = Object.values(districtData);

  // Navigate to specific dashboard tab
  const handleCardClick = (tab) => {
    setDbTab(tab);
    setView('dashboard');
  };

  // Generate chart data for recharts
  const getChartData = () => {
    return [
      { year: '2026', Demand: activeData.demand2026 },
      { year: '2028', Demand: activeData.demand2028 },
      { year: '2030', Demand: activeData.demand2030 },
    ];
  };

  // Chat message submission
  const handleSendChat = (textToSend) => {
    const query = textToSend || chatInput;
    if (!query.trim()) return;

    const newHistory = [...chatHistory, { sender: 'user', text: query }];
    setChatHistory(newHistory);
    if (!textToSend) setChatInput('');

    // Simulate smart bot response based on selected district
    setTimeout(() => {
      let botResponse = "";
      const lowerQuery = query.toLowerCase();

      if (lowerQuery.includes('priority') || lowerQuery.includes('score')) {
        botResponse = `The priority score for ${selectedDistrict} is currently ${activeData.priorityScore}/10. ${activeData.details} Its feasibility score is ${activeData.feasibility}.`;
      } else if (lowerQuery.includes('forecast') || lowerQuery.includes('future') || lowerQuery.includes('demand') || lowerQuery.includes('2030')) {
        botResponse = `Based on our machine learning models, EV charging demand in ${selectedDistrict} is projected to grow from ${activeData.demand2026} MWh in 2026 to ${activeData.demand2030} MWh by 2030. This represents a significant upward trend that warrants rapid infrastructure deployment.`;
      } else if (lowerQuery.includes('recommend') || lowerQuery.includes('place') || lowerQuery.includes('charger') || lowerQuery.includes('station')) {
        const recDetails = activeData.recs.map(r => `${r.count}x ${r.type} near ${r.area}`).join(', ');
        botResponse = `For ${selectedDistrict}, we recommend installing: ${recDetails}. Feasibility score is estimated at ${activeData.feasibility} based on grid capacity and road network metrics.`;
      } else {
        botResponse = `${selectedDistrict} currently has around ${activeData.evCount.toLocaleString()} active EVs. Our models recommend prioritizing ${activeData.recs[0]?.type || 'charging facilities'} in high-density sectors. Let me know if you would like details on priority scores, feasibility, or charging recommendations!`;
      }

      setChatHistory(prev => [...prev, { sender: 'bot', text: botResponse }]);
    }, 600);
  };

  return (
    <AnimatePresence mode="wait">
      {view === 'landing' ? (
        <motion.div
          key="landing"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.5 }}
          className="landing-container"
        >
          {/* Header */}
          <header className="landing-header">
            <div className="logo-container">
              <div className="logo-icon">
                <Zap />
              </div>
              <div className="logo-text">
                <span className="logo-title">EVision Telangana</span>
                <span className="logo-subtitle">AI-Powered EV Infrastructure Planner</span>
              </div>
            </div>
          </header>

          {/* Hero Content */}
          <main className="landing-hero">
            <div className="hero-left">
              <h1 className="hero-title">
                Smarter Decisions.
                <span>Greener Tomorrow.</span>
              </h1>
              <p className="hero-description">
                AI-driven insights to optimize EV charging station placement, 
                improve coverage, and build a sustainable future for Telangana.
              </p>
              <button 
                onClick={() => setView('dashboard')}
                className="explore-btn"
              >
                Explore Dashboard <ArrowRight />
              </button>
            </div>

            <div className="hero-right">
              {/* Card 1: AI Demand Forecasting */}
              <div 
                className="info-card"
                onClick={() => handleCardClick('forecasting')}
              >
                <div className="card-icon-container">
                  <TrendingUp />
                </div>
                <div className="card-content">
                  <h3 className="card-title">AI Demand Forecasting</h3>
                  <p className="card-desc">
                    Predict future EV charging demand across Telangana districts using machine learning models.
                  </p>
                </div>
              </div>

              {/* Card 2: Smart Recommendations */}
              <div 
                className="info-card"
                onClick={() => handleCardClick('recommendations')}
              >
                <div className="card-icon-container">
                  <Target />
                </div>
                <div className="card-content">
                  <h3 className="card-title">Smart Recommendations</h3>
                  <p className="card-desc">
                    Generate District Priority Scores to identify the best locations for new EV charging stations.
                  </p>
                </div>
              </div>

              {/* Card 3: AI Decision Assistant */}
              <div 
                className="info-card"
                onClick={() => handleCardClick('chatbot')}
              >
                <div className="card-icon-container">
                  <Bot />
                </div>
                <div className="card-content">
                  <h3 className="card-title">AI Decision Assistant</h3>
                  <p className="card-desc">
                    Ask questions in natural language and receive explainable insights into predictions and recommendations.
                  </p>
                </div>
              </div>
            </div>
          </main>
        </motion.div>
      ) : (
        <motion.div
          key="dashboard"
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -15 }}
          transition={{ duration: 0.4 }}
          className="dashboard-container"
        >
          {/* Dashboard Sidebar */}
          <aside className="db-sidebar">
            <div className="db-sidebar-logo">
              <div className="logo-icon">
                <Zap />
              </div>
              <div className="logo-text">
                <span className="logo-title">EVision</span>
                <span className="logo-subtitle" style={{color: '#64748b'}}>Telangana Planner</span>
              </div>
            </div>

            <nav className="db-nav">
              <button 
                onClick={() => setDbTab('overview')}
                className={`db-nav-item ${dbTab === 'overview' ? 'active' : ''}`}
              >
                <MapPin /> Overview & Map
              </button>
              <button 
                onClick={() => setDbTab('forecasting')}
                className={`db-nav-item ${dbTab === 'forecasting' ? 'active' : ''}`}
              >
                <ChartIcon /> Demand Forecasts
              </button>
              <button 
                onClick={() => setDbTab('recommendations')}
                className={`db-nav-item ${dbTab === 'recommendations' ? 'active' : ''}`}
              >
                <Layers /> Recommendations
              </button>
              <button 
                onClick={() => setDbTab('chatbot')}
                className={`db-nav-item ${dbTab === 'chatbot' ? 'active' : ''}`}
              >
                <MessageSquare /> AI Chat Assistant
              </button>
            </nav>

            <div className="db-sidebar-footer">
              <button 
                onClick={() => setView('landing')}
                className="back-to-landing-btn"
              >
                <ArrowLeft size={16} /> Back to Landing Page
              </button>
            </div>
          </aside>

          {/* Dashboard Main Window */}
          <main className="db-main">
            <header className="db-header">
              <div className="db-header-title">
                <h1>AI Planning Dashboard</h1>
              </div>

              {/* District Dropdown Selector */}
              <div style={{display: 'flex', alignItems: 'center', gap: '12px'}}>
                <span style={{fontSize: '13px', color: '#64748b', fontWeight: '500'}}>Active District:</span>
                <select
                  value={selectedDistrict}
                  onChange={(e) => setSelectedDistrict(e.target.value)}
                  className="district-selector"
                >
                  {Object.keys(districtData).map(d => (
                    <option key={d} value={d}>{d}</option>
                  ))}
                </select>
              </div>
            </header>

            <div className="db-content">
              {/* Key Metrics Row */}
              <div className="metrics-row">
                <div className="metric-card">
                  <div className="metric-icon-box">
                    <Target size={22} />
                  </div>
                  <div className="metric-info">
                    <span className="metric-label">Priority Score</span>
                    <span className="metric-value" style={{color: '#4ade80'}}>{activeData.priorityScore}/10</span>
                  </div>
                </div>

                <div className="metric-card">
                  <div className="metric-icon-box">
                    <Activity size={22} />
                  </div>
                  <div className="metric-info">
                    <span className="metric-label">Active EVs</span>
                    <span className="metric-value">{activeData.evCount.toLocaleString()}</span>
                  </div>
                </div>

                <div className="metric-card">
                  <div className="metric-icon-box">
                    <TrendingUp size={22} />
                  </div>
                  <div className="metric-info">
                    <span className="metric-label">2030 Demand Forecast</span>
                    <span className="metric-value">{activeData.demand2030} MWh</span>
                  </div>
                </div>

                <div className="metric-card">
                  <div className="metric-icon-box">
                    <ShieldCheck size={22} />
                  </div>
                  <div className="metric-info">
                    <span className="metric-label">Grid Feasibility</span>
                    <span className="metric-value">{activeData.feasibility}</span>
                  </div>
                </div>
              </div>

              {/* Dynamic Tabs view */}
              <div className="db-grid">
                
                {/* Left Panel: Map or Specific Detailed Info */}
                <div className="db-panel">
                  <h3 className="db-panel-title">
                    <Compass /> Interactive Planning Map
                  </h3>
                  
                  <div className="map-container">
                    <MapContainer 
                      center={[17.9784, 79.5941]} 
                      zoom={8} 
                      style={{ height: '100%', width: '100%' }}
                      zoomControl={false}
                    >
                      <TileLayer
                        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
                        url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
                      />
                      
                      {districtsList.map((d) => (
                        <CircleMarker
                          key={d.name}
                          center={d.coordinates}
                          radius={d.name === selectedDistrict ? 16 : 10}
                          fillColor={d.name === selectedDistrict ? '#22c55e' : '#15803d'}
                          color={d.name === selectedDistrict ? '#ffffff' : '#4ade80'}
                          weight={d.name === selectedDistrict ? 3 : 1}
                          opacity={0.8}
                          fillOpacity={0.6}
                          eventHandlers={{
                            click: () => {
                              setSelectedDistrict(d.name);
                            },
                          }}
                        >
                          <Popup>
                            <div style={{ padding: '4px', textAlign: 'left' }}>
                              <h4 style={{ margin: '0 0 6px 0', fontSize: '14px', fontWeight: '700', color: 'var(--dark)' }}>
                                {d.name} District
                              </h4>
                              <p style={{ margin: '0 0 4px 0', fontSize: '12px', color: 'var(--muted)' }}>
                                <b>Priority Score:</b> {d.priorityScore}/10
                              </p>
                              <p style={{ margin: '0', fontSize: '12px', color: 'var(--muted)' }}>
                                <b>EV Count:</b> {d.evCount.toLocaleString()}
                              </p>
                            </div>
                          </Popup>
                        </CircleMarker>
                      ))}

                      {/* Pans map to active district when selected from sidebar dropdown */}
                      <ChangeView center={activeData.coordinates} />
                    </MapContainer>
                  </div>
                </div>

                {/* Right Panel: Updates dynamically based on dbTab */}
                <div className="db-panel">
                  
                  {dbTab === 'overview' && (
                    <div style={{display: 'flex', flexDirection: 'column', gap: '16px', height: '100%'}}>
                      <h3 className="db-panel-title"><Layers /> District Profile: {selectedDistrict}</h3>
                      <p style={{fontSize: '13.5px', color: 'var(--muted)', lineHeight: '1.5', margin: '0 0 8px 0'}}>
                        {activeData.details}
                      </p>
                      
                      <h4 style={{fontSize: '13px', fontWeight: '700', textTransform: 'uppercase', color: 'var(--muted)', margin: '8px 0 4px 0'}}>
                        Target Installations
                      </h4>
                      <div className="recs-list" style={{flex: 1}}>
                        {activeData.recs.map((r, i) => (
                          <div key={i} className="rec-item">
                            <div className="rec-header">
                              <span className="rec-title">{r.type}</span>
                              <span className="rec-badge high" style={{
                                backgroundColor: r.count > 40 ? 'rgba(239, 68, 68, 0.15)' : 'rgba(245, 158, 11, 0.15)',
                                color: r.count > 40 ? '#f87171' : '#fbbf24'
                              }}>
                                {r.count} Stations
                              </span>
                            </div>
                            <span className="rec-desc">Primary Deployment Area: <b>{r.area}</b></span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {dbTab === 'forecasting' && (
                    <div style={{display: 'flex', flexDirection: 'column', gap: '16px', height: '100%'}}>
                      <h3 className="db-panel-title"><TrendingUp /> ML Demand Forecasting (MWh)</h3>
                      <p style={{fontSize: '13px', color: 'var(--muted)', margin: 0}}>
                        Projected grid capacity allocation needed for {selectedDistrict} from 2026 to 2030.
                      </p>
                      
                      <div style={{flex: 1, minHeight: '260px', marginTop: '16px'}}>
                        <ResponsiveContainer width="100%" height="95%">
                          <LineChart data={getChartData()} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
                            <XAxis dataKey="year" stroke="var(--muted)" fontSize={12} />
                            <YAxis stroke="var(--muted)" fontSize={12} />
                            <Tooltip 
                              contentStyle={{ backgroundColor: '#ffffff', borderColor: 'var(--border)', color: 'var(--dark)' }}
                              labelStyle={{ color: 'var(--primary)', fontWeight: 'bold' }}
                            />
                            <Legend verticalAlign="top" height={36} iconType="circle" />
                            <Line 
                              type="monotone" 
                              dataKey="Demand" 
                              stroke="var(--primary)" 
                              strokeWidth={3} 
                              activeDot={{ r: 8 }} 
                              dot={{ strokeWidth: 2, r: 4 }}
                            />
                          </LineChart>
                        </ResponsiveContainer>
                      </div>
                      
                      <div style={{backgroundColor: 'rgba(34, 197, 94, 0.05)', padding: '12px', border: '1px solid rgba(34, 197, 94, 0.15)', borderRadius: '8px', fontSize: '12.5px', color: '#4ade80'}}>
                        💡 <b>AI Analysis:</b> Demand is growing rapidly. We recommend scheduling substation reinforcements before Q3 2028 to accommodate local EV load spikes.
                      </div>
                    </div>
                  )}

                  {dbTab === 'recommendations' && (
                    <div style={{display: 'flex', flexDirection: 'column', gap: '16px', height: '100%'}}>
                      <h3 className="db-panel-title"><Target /> Feasibility & Site Recommendations</h3>
                      
                      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px', margin: '4px 0'}}>
                        <div style={{backgroundColor: '#ffffff', padding: '14px', borderRadius: '8px', border: '1px solid var(--border)', boxShadow: '0 1px 3px rgba(0,0,0,0.02)'}}>
                          <div style={{fontSize: '11px', color: 'var(--muted)', fontWeight: '600'}}>LAND AVAILABILITY</div>
                          <div style={{fontSize: '16px', fontWeight: '700', color: 'var(--dark)', marginTop: '4px'}}>High Feasibility</div>
                        </div>
                        <div style={{backgroundColor: '#ffffff', padding: '14px', borderRadius: '8px', border: '1px solid var(--border)', boxShadow: '0 1px 3px rgba(0,0,0,0.02)'}}>
                          <div style={{fontSize: '11px', color: 'var(--muted)', fontWeight: '600'}}>GRID CONNECTION</div>
                          <div style={{fontSize: '16px', fontWeight: '700', color: 'var(--dark)', marginTop: '4px'}}>Ready Capacity</div>
                        </div>
                      </div>

                      <p style={{fontSize: '13px', color: 'var(--muted)', lineHeight: '1.4', margin: 0}}>
                        Our spatial optimization engine suggests the following exact locations for optimal chargers:
                      </p>

                      <div className="recs-list" style={{flex: 1}}>
                        {activeData.recs.map((r, i) => (
                          <div key={i} className="rec-item">
                            <div className="rec-header">
                              <span className="rec-title">{r.type}</span>
                              <span className="rec-badge" style={{backgroundColor: 'rgba(34, 197, 94, 0.15)', color: '#4ade80'}}>
                                Match Rate: 98%
                              </span>
                            </div>
                            <span className="rec-desc">Optimal Site Coordinates: <b>{activeData.coordinates[0].toFixed(4)}, {activeData.coordinates[1].toFixed(4)}</b> (Within {r.area})</span>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {dbTab === 'chatbot' && (
                    <div className="chat-panel">
                      <h3 className="db-panel-title"><Bot /> AI Decision Assistant</h3>
                      
                      {/* Chat History */}
                      <div className="chat-history">
                        {chatHistory.map((msg, index) => (
                          <div key={index} className={`chat-message ${msg.sender}`}>
                            {msg.text}
                          </div>
                        ))}
                        <div ref={chatEndRef} />
                      </div>

                      {/* Quick Suggestions Buttons */}
                      <div className="chat-suggestions">
                        <button 
                          onClick={() => handleSendChat(`What is the priority score for ${selectedDistrict}?`)}
                          className="chat-suggest-btn"
                        >
                          Show Priority Score
                        </button>
                        <button 
                          onClick={() => handleSendChat(`Where should we install chargers in ${selectedDistrict}?`)}
                          className="chat-suggest-btn"
                        >
                          Charging Recommendations
                        </button>
                        <button 
                          onClick={() => handleSendChat(`What is the demand forecast for ${selectedDistrict}?`)}
                          className="chat-suggest-btn"
                        >
                          Demand Forecast
                        </button>
                      </div>

                      {/* Input area */}
                      <div className="chat-input-row">
                        <input
                          type="text"
                          value={chatInput}
                          onChange={(e) => setChatInput(e.target.value)}
                          onKeyDown={(e) => e.key === 'Enter' && handleSendChat()}
                          placeholder="Ask a question about district planning..."
                          className="chat-input"
                        />
                        <button 
                          onClick={() => handleSendChat()}
                          className="chat-send-btn"
                        >
                          <Send size={18} />
                        </button>
                      </div>
                    </div>
                  )}

                </div>

              </div>

            </div>
          </main>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

export default App;
