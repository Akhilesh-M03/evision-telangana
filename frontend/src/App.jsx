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
  Compass,
  LayoutDashboard,
  Map,
  BarChart2,
  ChevronLeft,
  ChevronRight,
  Search,
  Moon,
  AlertTriangle,
  ZoomIn,
  ZoomOut,
  Maximize2,
  ArrowUpRight,
  Sparkles,
  Calendar,
  ChevronDown,
  Download,
  Check,
  Clock
} from 'lucide-react';
import { MapContainer, TileLayer, CircleMarker, Popup, useMap, GeoJSON } from 'react-leaflet';
import { 
  ResponsiveContainer, 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend,
  AreaChart,
  Area,
  Cell,
  PieChart,
  Pie,
  BarChart,
  Bar
} from 'recharts';

import 'leaflet/dist/leaflet.css';
import figCleanBoth from './assets/fig_clean_both.png';
import evChargingVector from './assets/ev_charging_station_vector.png';

// Realistic mock data for Telangana districts
const districtData = {
  "Hyderabad": {
    name: "Hyderabad",
    coordinates: [17.3606, 78.4741],
    priorityScore: 9.6,
    evCount: 24500,
    demand2026: 42,
    demand2028: 82,
    demand2030: 120,
    recs: [
      { type: "DC Ultra-Fast (150kW)", count: 45, area: "IT Corridors, Malls" },
      { type: "DC Fast (50kW)", count: 105, area: "Metro Stations, Commercial Hubs" },
      { type: "AC Type 2 (22kW)", count: 300, area: "Residential Societies, Office Parks" }
    ],
    details: "Critical priority due to high density of electric two-wheelers and passenger vehicles. Focus placement near high-traffic IT parks (Gachibowli, Hitec City) and major commercial centers.",
    feasibility: "94%",
    priorityLevel: "critical"
  },
  "Rangareddy": {
    name: "Rangareddy",
    coordinates: [17.1334, 78.3971],
    priorityScore: 9.1,
    evCount: 18200,
    demand2026: 36,
    demand2028: 68,
    demand2030: 95,
    recs: [
      { type: "DC Ultra-Fast (150kW)", count: 30, area: "Outer Ring Road (ORR) Plazas" },
      { type: "DC Fast (50kW)", count: 80, area: "Transit Hubs, Highway Nodes" },
      { type: "AC Type 2 (22kW)", count: 220, area: "Tech Parks, Gated Communities" }
    ],
    details: "Very high priority. High demand growth along transit corridors and peripheral highways. Highly suitable for solar-powered highway charging stations.",
    feasibility: "89%",
    priorityLevel: "critical"
  },
  "Medchal-Malkajgiri": {
    name: "Medchal-Malkajgiri",
    coordinates: [17.6340, 78.4843],
    priorityScore: 8.8,
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
    feasibility: "86%",
    priorityLevel: "critical"
  },
  "Sangareddy": {
    name: "Sangareddy",
    coordinates: [17.8684, 77.8227],
    priorityScore: 8.3,
    evCount: 9200,
    demand2026: 24,
    demand2028: 45,
    demand2030: 68,
    recs: [
      { type: "DC Ultra-Fast (150kW)", count: 15, area: "NH-65 Highway Junctions" },
      { type: "DC Fast (50kW)", count: 45, area: "Sangareddy City Hub, Bus Stand" },
      { type: "AC Type 2 (22kW)", count: 110, area: "IIT Kandi, Residential Sectors" }
    ],
    details: "High priority. Rapid growth along the industrial corridor and close connection to Hyderabad Outer Ring Road.",
    feasibility: "83%",
    priorityLevel: "high"
  },
  "Siddipet": {
    name: "Siddipet",
    coordinates: [18.0056, 78.8961],
    priorityScore: 8.0,
    evCount: 7800,
    demand2026: 22,
    demand2028: 42,
    demand2030: 63,
    recs: [
      { type: "DC Fast (50kW)", count: 35, area: "Siddipet Bypass Road, Market Yard" },
      { type: "AC Type 2 (22kW)", count: 90, area: "Public Offices, Residential Colonies" }
    ],
    details: "High priority. Developing administrative and urban center showing high EV registration trends.",
    feasibility: "82%",
    priorityLevel: "high"
  },
  "Medak": {
    name: "Medak",
    coordinates: [17.9375, 78.2117],
    priorityScore: 7.9,
    evCount: 7100,
    demand2026: 21,
    demand2028: 39,
    demand2030: 58,
    recs: [
      { type: "DC Fast (50kW)", count: 30, area: "Medak Cathedral Zone, Main Bus Station" },
      { type: "AC Type 2 (22kW)", count: 80, area: "Town Hubs, Tourist Spots" }
    ],
    details: "High priority. Steady growth driven by light industrial activities and regional transit infrastructure.",
    feasibility: "81%",
    priorityLevel: "high"
  },
  "Warangal Urban": {
    name: "Warangal Urban",
    coordinates: [18.0327, 79.4284],
    priorityScore: 7.7,
    evCount: 11500,
    demand2026: 24,
    demand2028: 45,
    demand2030: 67,
    recs: [
      { type: "DC Fast (50kW)", count: 45, area: "Hanumakonda, Kazipet Junction" },
      { type: "AC Type 2 (22kW)", count: 120, area: "NIT Campus, Commercial Complexes" }
    ],
    details: "High priority. The second-largest urban cluster in Telangana. Grid capacity is strong and ready for fast charging infrastructure.",
    feasibility: "85%",
    priorityLevel: "high"
  },
  "Nizamabad": {
    name: "Nizamabad",
    coordinates: [18.6732, 78.0978],
    priorityScore: 7.6,
    evCount: 8900,
    demand2026: 18,
    demand2028: 36,
    demand2030: 54,
    recs: [
      { type: "DC Fast (50kW)", count: 32, area: "NH-44 Corridor, City Bypass" },
      { type: "AC Type 2 (22kW)", count: 28, area: "Distributor Points, Main Market" }
    ],
    details: "High priority agricultural and trading hub. Potential for cargo EV fleet charging along NH-44.",
    feasibility: "80%",
    priorityLevel: "high"
  },
  "Nalgonda": {
    name: "Nalgonda",
    coordinates: [17.0504, 79.2669],
    priorityScore: 7.4,
    evCount: 9800,
    demand2026: 20,
    demand2028: 38,
    demand2030: 59,
    recs: [
      { type: "DC Fast (50kW)", count: 38, area: "Hyderabad-Vijayawada Highway (NH-65)" },
      { type: "AC Type 2 (22kW)", count: 100, area: "Local Bus Stands, Public Offices" }
    ],
    details: "High priority. Heavily reliant on highway transit corridor demand. Highly strategic for fast chargers on NH-65.",
    feasibility: "79%",
    priorityLevel: "high"
  },
  "Kamareddy": {
    name: "Kamareddy",
    coordinates: [18.3166, 78.0539],
    priorityScore: 7.3,
    evCount: 6200,
    demand2026: 16,
    demand2028: 32,
    demand2030: 48,
    recs: [
      { type: "DC Fast (50kW)", count: 22, area: "Kamareddy Highway Junction" },
      { type: "AC Type 2 (22kW)", count: 70, area: "Town Commercial Centers" }
    ],
    details: "High priority. Steady local growth along the northern NH-44 highway route.",
    feasibility: "78%",
    priorityLevel: "high"
  },
  "Yadadri Bhuvanagiri": {
    name: "Yadadri Bhuvanagiri",
    coordinates: [17.5173, 78.8863],
    priorityScore: 6.9,
    evCount: 6500,
    demand2026: 15,
    demand2028: 28,
    demand2030: 44,
    recs: [
      { type: "DC Fast (50kW)", count: 20, area: "Yadadri Temple Parking, NH-163" },
      { type: "AC Type 2 (22kW)", count: 65, area: "Tourist Rest Stops, Town Center" }
    ],
    details: "Medium priority. High pilgrim transit traffic makes it a prime candidate for public charging hubs.",
    feasibility: "77%",
    priorityLevel: "medium"
  },
  "Vikarabad": {
    name: "Vikarabad",
    coordinates: [17.2703, 77.7453],
    priorityScore: 6.7,
    evCount: 4800,
    demand2026: 12,
    demand2028: 24,
    demand2030: 36,
    recs: [
      { type: "DC Fast (50kW)", count: 14, area: "Vikarabad Station Road, Ananthagiri Hills" },
      { type: "AC Type 2 (22kW)", count: 50, area: "Resorts Area, District Collectorate" }
    ],
    details: "Medium priority. Popular tourist getaway from Hyderabad with a growing requirement for weekend destination charging.",
    feasibility: "76%",
    priorityLevel: "medium"
  },
  "Warangal Rural": {
    name: "Warangal Rural",
    coordinates: [17.9821, 79.5971],
    priorityScore: 6.6,
    evCount: 5200,
    demand2026: 13,
    demand2028: 25,
    demand2030: 38,
    recs: [
      { type: "DC Fast (50kW)", count: 15, area: "National Highway Bypass Nodes" },
      { type: "AC Type 2 (22kW)", count: 55, area: "Rural Markets, Sub-station Hubs" }
    ],
    details: "Medium priority. Surrounding agricultural logistics hubs require fast charging deployment for light trucks.",
    feasibility: "74%",
    priorityLevel: "medium"
  },
  "Suryapet": {
    name: "Suryapet",
    coordinates: [17.0800, 79.7925],
    priorityScore: 6.5,
    evCount: 6800,
    demand2026: 14,
    demand2028: 27,
    demand2030: 41,
    recs: [
      { type: "DC Fast (50kW)", count: 18, area: "NH-65 Highway Food Courts" },
      { type: "AC Type 2 (22kW)", count: 60, area: "Suryapet City Center" }
    ],
    details: "Medium priority. Highly strategic stopover midway between Hyderabad and Vijayawada on NH-65.",
    feasibility: "75%",
    priorityLevel: "medium"
  },
  "Nagarkurnool": {
    name: "Nagarkurnool",
    coordinates: [16.4158, 78.6830],
    priorityScore: 6.4,
    evCount: 4200,
    demand2026: 10,
    demand2028: 20,
    demand2030: 30,
    recs: [
      { type: "DC Fast (50kW)", count: 12, area: "Srisailam Highway Route, Town Bus Stand" },
      { type: "AC Type 2 (22kW)", count: 45, area: "District Offices, Local Markets" }
    ],
    details: "Medium priority. Significant transit traffic along the forest/temple tourism routes.",
    feasibility: "73%",
    priorityLevel: "medium"
  },
  "Jangaon": {
    name: "Jangaon",
    coordinates: [17.7466, 79.2407],
    priorityScore: 6.3,
    evCount: 3800,
    demand2026: 9,
    demand2028: 18,
    demand2030: 28,
    recs: [
      { type: "DC Fast (50kW)", count: 10, area: "Jangaon Bypass, Station Road" },
      { type: "AC Type 2 (22kW)", count: 40, area: "Town Sub-station, Offices" }
    ],
    details: "Medium priority. Rapid transit connection node between Hyderabad and Warangal.",
    feasibility: "72%",
    priorityLevel: "medium"
  },
  "Khammam": {
    name: "Khammam",
    coordinates: [17.2465, 80.1500],
    priorityScore: 6.2,
    evCount: 8200,
    demand2026: 16,
    demand2028: 30,
    demand2030: 46,
    recs: [
      { type: "DC Fast (50kW)", count: 20, area: "Town Entrance, Main Market" },
      { type: "AC Type 2 (22kW)", count: 70, area: "District Hospital, Shopping Streets" }
    ],
    details: "Medium priority. Large urban and trading municipality with steady EV fleet expansion.",
    feasibility: "77%",
    priorityLevel: "medium"
  },
  "Mahbubnagar": {
    name: "Mahbubnagar",
    coordinates: [16.7435, 77.9923],
    priorityScore: 6.1,
    evCount: 7900,
    demand2026: 15,
    demand2028: 29,
    demand2030: 43,
    recs: [
      { type: "DC Fast (50kW)", count: 18, area: "Mahbubnagar Bypass, Railway Station" },
      { type: "AC Type 2 (22kW)", count: 65, area: "Industrial Area, Town Centers" }
    ],
    details: "Medium priority. Expanding commercial center linking southern districts to Hyderabad.",
    feasibility: "76%",
    priorityLevel: "medium"
  },
  "Peddapalli": {
    name: "Peddapalli",
    coordinates: [18.6207, 79.4950],
    priorityScore: 6.0,
    evCount: 5100,
    demand2026: 11,
    demand2028: 21,
    demand2030: 32,
    recs: [
      { type: "DC Fast (50kW)", count: 12, area: "NTPC Ramagundam Sector, Town Markets" },
      { type: "AC Type 2 (22kW)", count: 48, area: "Residential Colonies, Office Parks" }
    ],
    details: "Medium priority industrial zone. High capacity grid infrastructure is already present.",
    feasibility: "75%",
    priorityLevel: "medium"
  },
  "Wanaparthy": {
    name: "Wanaparthy",
    coordinates: [16.2853, 77.9864],
    priorityScore: 5.8,
    evCount: 3200,
    demand2026: 8,
    demand2028: 15,
    demand2030: 23,
    recs: [
      { type: "DC Fast (50kW)", count: 8, area: "Wanaparthy Bypass, Collectorate" },
      { type: "AC Type 2 (22kW)", count: 35, area: "Government College Campus" }
    ],
    details: "Medium priority. Steady suburban demand with focus on agricultural logistics transport.",
    feasibility: "71%",
    priorityLevel: "medium"
  },
  "Rajanna Sircilla": {
    name: "Rajanna Sircilla",
    coordinates: [18.3898, 78.8086],
    priorityScore: 5.7,
    evCount: 3900,
    demand2026: 9,
    demand2028: 16,
    demand2030: 25,
    recs: [
      { type: "DC Fast (50kW)", count: 9, area: "Textile Cluster, Sircilla Bus Stand" },
      { type: "AC Type 2 (22kW)", count: 40, area: "Industrial Sheds, Town Parkings" }
    ],
    details: "Medium priority. High concentrations of textile industries. Focus on commercial three-wheeler charging.",
    feasibility: "72%",
    priorityLevel: "medium"
  },
  "Karimnagar": {
    name: "Karimnagar",
    coordinates: [18.4348, 79.1328],
    priorityScore: 5.5,
    evCount: 6500,
    demand2026: 12,
    demand2028: 24,
    demand2030: 36,
    recs: [
      { type: "DC Fast (50kW)", count: 15, area: "Karimnagar Bus Station, Bypass Road" },
      { type: "AC Type 2 (22kW)", count: 50, area: "Residential Layouts, Municipal Parkings" }
    ],
    details: "Medium priority. Strong agricultural trade hub. Focus on connecting highways to Hyderabad.",
    feasibility: "74%",
    priorityLevel: "medium"
  },
  "Mahabubabad": {
    name: "Mahabubabad",
    coordinates: [17.7139, 80.0413],
    priorityScore: 5.1,
    evCount: 2900,
    demand2026: 6,
    demand2028: 12,
    demand2030: 19,
    recs: [
      { type: "DC Fast (50kW)", count: 7, area: "Mahabubabad Station Area" },
      { type: "AC Type 2 (22kW)", count: 30, area: "Town Markets" }
    ],
    details: "Low-medium priority. Focus on public transit electrification (e-autos and e-rickshaws).",
    feasibility: "68%",
    priorityLevel: "low"
  },
  "Jagtial": {
    name: "Jagtial",
    coordinates: [18.8214, 78.9151],
    priorityScore: 4.9,
    evCount: 3100,
    demand2026: 7,
    demand2028: 13,
    demand2030: 20,
    recs: [
      { type: "DC Fast (50kW)", count: 8, area: "Jagtial Bus Station, Bypass Road" },
      { type: "AC Type 2 (22kW)", count: 32, area: "Municipal Parking, Town Hub" }
    ],
    details: "Low priority. Moderate demand. Primary focus on two-wheeler and public transit hubs.",
    feasibility: "67%",
    priorityLevel: "low"
  },
  "Bhadradri KG": {
    name: "Bhadradri KG",
    coordinates: [17.5513, 80.6145],
    priorityScore: 4.8,
    evCount: 3800,
    demand2026: 8,
    demand2028: 15,
    demand2030: 23,
    recs: [
      { type: "DC Fast (50kW)", count: 10, area: "Kothagudem Town Entrance, Bhadrachalam Temple Route" },
      { type: "AC Type 2 (22kW)", count: 35, area: "Colliery Colonies, Hospital Road" }
    ],
    details: "Low priority. Industrial mining zones showing steady freight fleet requirements.",
    feasibility: "68%",
    priorityLevel: "low"
  },
  "Mulugu": {
    name: "Mulugu",
    coordinates: [18.3145, 80.3459],
    priorityScore: 4.7,
    evCount: 1800,
    demand2026: 4,
    demand2028: 8,
    demand2030: 13,
    recs: [
      { type: "DC Fast (50kW)", count: 5, area: "Ramappa Temple Tourism Stop" },
      { type: "AC Type 2 (22kW)", count: 20, area: "Forest Gateways, Local Bazaar" }
    ],
    details: "Low priority. Eco-tourism district with seasonal demand peaks around cultural heritage sites.",
    feasibility: "65%",
    priorityLevel: "low"
  },
  "Mancherial": {
    name: "Mancherial",
    coordinates: [18.9813, 79.5198],
    priorityScore: 4.6,
    evCount: 2800,
    demand2026: 6,
    demand2028: 11,
    demand2030: 18,
    recs: [
      { type: "DC Fast (50kW)", count: 8, area: "Railway Station Plaza, Coalfields Bypass" },
      { type: "AC Type 2 (22kW)", count: 28, area: "Local Market Square" }
    ],
    details: "Low priority. Mining belt with primary demand originating from utility cargo transport.",
    feasibility: "66%",
    priorityLevel: "low"
  },
  "Jogulamba Gadwal": {
    name: "Jogulamba Gadwal",
    coordinates: [16.2347, 77.7946],
    priorityScore: 4.5,
    evCount: 2200,
    demand2026: 5,
    demand2028: 10,
    demand2030: 15,
    recs: [
      { type: "DC Fast (50kW)", count: 6, area: "NH-44 Highway Interchange, Temple Gate" },
      { type: "AC Type 2 (22kW)", count: 22, area: "Town Center Markets" }
    ],
    details: "Low priority. Southern border transition point on NH-44 with strategic transient demand.",
    feasibility: "64%",
    priorityLevel: "low"
  },
  "Jayashankar": {
    name: "Jayashankar",
    coordinates: [18.4381, 79.8685],
    priorityScore: 4.4,
    evCount: 1900,
    demand2026: 4,
    demand2028: 8,
    demand2030: 13,
    recs: [
      { type: "DC Fast (50kW)", count: 5, area: "Bhupalpally Mining Area" },
      { type: "AC Type 2 (22kW)", count: 20, area: "Forest Rest Houses, Local Markets" }
    ],
    details: "Low priority. Rural district with limited grid capacity. Recommend lightweight AC charging stations.",
    feasibility: "62%",
    priorityLevel: "low"
  },
  "Nirmal": {
    name: "Nirmal",
    coordinates: [19.0915, 78.3966],
    priorityScore: 4.3,
    evCount: 2100,
    demand2026: 5,
    demand2028: 9,
    demand2030: 14,
    recs: [
      { type: "DC Fast (50kW)", count: 6, area: "Nirmal Toy Cluster, NH-44 Route" },
      { type: "AC Type 2 (22kW)", count: 24, area: "Artisans Colony, Local Hub" }
    ],
    details: "Low priority. Cultural handicraft town. Initial infrastructure deployment along NH-44 bypass is recommended.",
    feasibility: "63%",
    priorityLevel: "low"
  },
  "Narayanpet": {
    name: "Narayanpet",
    coordinates: [16.7006, 77.6165],
    priorityScore: 4.2,
    evCount: 1700,
    demand2026: 4,
    demand2028: 8,
    demand2030: 12,
    recs: [
      { type: "DC Fast (50kW)", count: 5, area: "Narayanpet Handloom Cluster" },
      { type: "AC Type 2 (22kW)", count: 18, area: "Town Bus Stand Parking" }
    ],
    details: "Low priority. Border trade hub with initial requirements centered on local commercial transport.",
    feasibility: "61%",
    priorityLevel: "low"
  },
  "Komaram Bheem": {
    name: "Komaram Bheem",
    coordinates: [19.3593, 79.2960],
    priorityScore: 4.0,
    evCount: 1400,
    demand2026: 3,
    demand2028: 6,
    demand2030: 9,
    recs: [
      { type: "DC Fast (50kW)", count: 4, area: "Asifabad Main Road" },
      { type: "AC Type 2 (22kW)", count: 15, area: "Local Municipal Offices" }
    ],
    details: "Low priority. Remote forest district. Primary focus on charging stations at government administration offices.",
    feasibility: "58%",
    priorityLevel: "low"
  },
  "Adilabad": {
    name: "Adilabad",
    coordinates: [19.6759, 78.5340],
    priorityScore: 3.8,
    evCount: 1600,
    demand2026: 4,
    demand2028: 7,
    demand2030: 11,
    recs: [
      { type: "DC Fast (50kW)", count: 5, area: "Adilabad Town Entrance, Collectorate" },
      { type: "AC Type 2 (22kW)", count: 18, area: "Local Cotton Market Yard" }
    ],
    details: "Low priority northern border district. Focus on connecting roads to Maharashtra and public hubs.",
    feasibility: "55%",
    priorityLevel: "low"
  }
};;

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

const DEMAND_DATA = [
  { month: "Jan", actual: 0.82, forecast: 0.85 },
  { month: "Feb", actual: 0.88, forecast: 0.91 },
  { month: "Mar", actual: 0.94, forecast: 0.96 },
  { month: "Apr", actual: 1.02, forecast: 1.05 },
  { month: "May", actual: 1.08, forecast: 1.12 },
  { month: "Jun", actual: 1.18, forecast: 1.20 },
  { month: "Jul", actual: null, forecast: 1.24 },
  { month: "Aug", actual: null, forecast: 1.31 },
  { month: "Sep", actual: null, forecast: 1.38 },
];

function App() {
  const [view, setView] = useState('landing'); // 'landing' or 'dashboard'
  const [dbTab, setDbTab] = useState('dashboard'); // 'dashboard', 'explorer', 'predictions', 'analytics', 'assistant'
  const [selectedDistrict, setSelectedDistrict] = useState('Hyderabad');
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
  
  // Chat state
  const [chatHistory, setChatHistory] = useState([
    {
      sender: 'bot',
      text: "Greeting",
      isGreeting: true
    },
    {
      sender: 'user',
      text: "Which districts should be prioritized for new charging stations?",
      timestamp: "10:24 AM"
    },
    {
      sender: 'bot',
      text: "Based on AI analysis of demand, capacity gap, growth potential, and infrastructure readiness, the top priority districts for new charging stations are:",
      showTable: true,
      subtext: "These districts show high future demand and significant infrastructure gaps. Would you like me to show detailed insights for any of these districts?",
      timestamp: "10:24 AM"
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

  const [geojsonData, setGeojsonData] = useState(null);

  useEffect(() => {
    fetch('/telangana.geojson')
      .then(res => res.json())
      .then(data => {
        setGeojsonData(data);
      })
      .catch(err => console.error("Error loading Telangana GeoJSON:", err));
  }, []);


  const styleDistrictFeature = (feature) => {
    const districtName = feature.properties.D_NAME;
    let normalizedName = districtName;
    if (districtName === "Jayashankar") normalizedName = "Jayashankar Bhupalpally";
    else if (districtName === "Yadadri Badrari") normalizedName = "Yadadri Bhuvanagiri";
    else if (districtName === "Komaram Bheem") normalizedName = "Kumuram Bheem Asifabad";
    else if (districtName === "Medchal Malkajgiri") normalizedName = "Medchal-Malkajgiri";
    else if (districtName === "Warangal Urban") normalizedName = "Warangal Hanamkonda";
    else if (districtName === "Warangal Rural") normalizedName = "Warangal";
    
    const dData = districtData[normalizedName] || 
                  Object.values(districtData).find(d => d.name.toLowerCase() === normalizedName.toLowerCase());
    
    const priorityLevel = dData ? dData.priorityLevel : 'low';
    const fillColor = getPriorityColor(priorityLevel);
    
    const isActive = selectedDistrict.toLowerCase() === normalizedName.toLowerCase() || 
                   (dData && dData.name === selectedDistrict);
    
    return {
      fillColor: fillColor,
      weight: isActive ? 2.5 : 1.2,
      opacity: 1,
      color: isActive ? '#0f172a' : '#ffffff',
      fillOpacity: isActive ? 0.8 : 0.55,
    };
  };

  const onEachDistrictFeature = (feature, layer) => {
    const districtName = feature.properties.D_NAME;
    let normalizedName = districtName;
    if (districtName === "Jayashankar") normalizedName = "Jayashankar Bhupalpally";
    else if (districtName === "Yadadri Badrari") normalizedName = "Yadadri Bhuvanagiri";
    else if (districtName === "Komaram Bheem") normalizedName = "Kumuram Bheem Asifabad";
    else if (districtName === "Medchal Malkajgiri") normalizedName = "Medchal-Malkajgiri";
    else if (districtName === "Warangal Urban") normalizedName = "Warangal Hanamkonda";
    else if (districtName === "Warangal Rural") normalizedName = "Warangal";
    
    const dData = districtData[normalizedName] || 
                  Object.values(districtData).find(d => d.name.toLowerCase() === normalizedName.toLowerCase());
    
    const displayName = dData ? dData.name : districtName;

    layer.on({
      click: () => {
        setSelectedDistrict(displayName);
      },
      mouseover: (e) => {
        const l = e.target;
        l.setStyle({
          fillOpacity: 0.85,
          weight: 2.2
        });
      },
      mouseout: (e) => {
        const l = e.target;
        const isActive = displayName === selectedDistrict;
        l.setStyle({
          fillOpacity: isActive ? 0.8 : 0.55,
          weight: isActive ? 2.5 : 1.2
        });
      }
    });

    const majorDistricts = [
      "Adilabad", "Nizamabad", "Karimnagar", "Warangal", "Khammam", 
      "Nalgonda", "Mahabubnagar", "Sangareddy", "Rangareddy", 
      "Medchal-Malkajgiri", "Hyderabad"
    ];

    const isMajor = majorDistricts.some(md => md.toLowerCase() === displayName.toLowerCase());

    if (isMajor) {
      layer.bindTooltip(displayName, {
        permanent: true,
        direction: 'center',
        className: 'district-tooltip-label'
      });
    } else {
      layer.bindTooltip(displayName, {
        permanent: false,
        direction: 'top',
        className: 'district-tooltip-hover'
      });
    }
  };

  // Translate original landing page card clicks to new tabs
  const handleCardClick = (tab) => {
    if (tab === 'forecasting') setDbTab('predictions');
    else if (tab === 'recommendations') setDbTab('explorer');
    else if (tab === 'chatbot') setDbTab('assistant');
    else setDbTab(tab);
    setView('dashboard');
  };

  // Generate chart data for predictions
  const getChartData = () => {
    return [
      { year: '2026', Demand: activeData.demand2026 },
      { year: '2028', Demand: activeData.demand2028 },
      { year: '2030', Demand: activeData.demand2030 },
    ];
  };

  // Generate monthly demand trend data from Jan '25 to Nov '26
  const getForecastTrendData = () => {
    const baseVal = activeData.demand2026 / 35;
    const months = [
      "Jan '25", "Mar '25", "May '25", "Jul '25", "Sep '25", "Nov '25",
      "Jan '26", "Mar '26", "May '26", "Jul '26", "Sep '26", "Nov '26"
    ];
    return months.map((month, idx) => {
      const growthFactor = 0.5 + idx * 0.08;
      const val = baseVal * growthFactor * (0.95 + Math.sin(idx * 0.8) * 0.03);
      let actual = null;
      let forecast = null;
      if (idx <= 4) {
        actual = parseFloat(val.toFixed(2));
        if (idx === 4) {
          forecast = actual;
        }
      } else {
        forecast = parseFloat(val.toFixed(2));
      }
      return { month, actual, forecast };
    });
  };

  // Generate AreaChart data for Dashboard
  const getAreaChartData = () => {
    const factor = activeData.demand2030 / 120.0;
    return DEMAND_DATA.map(d => ({
      ...d,
      actual: d.actual ? parseFloat((d.actual * factor * 10).toFixed(1)) : null,
      forecast: d.forecast ? parseFloat((d.forecast * factor * 10).toFixed(1)) : null,
    }));
  };

  // Generate Analytics tab comparison data
  const getTopDistrictsData = () => {
    return districtsList
      .sort((a, b) => b.demand2030 - a.demand2030)
      .slice(0, 5)
      .map(d => ({
        name: d.name,
        Demand: d.demand2030,
        EVs: d.evCount
      }));
  };

  // Chat message submission
  const handleSendChat = (textToSend) => {
    const query = textToSend || chatInput;
    if (!query.trim()) return;

    // Get current formatted time
    const now = new Date();
    const formattedTime = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    const newHistory = [...chatHistory, { sender: 'user', text: query, timestamp: formattedTime }];
    setChatHistory(newHistory);
    if (!textToSend) setChatInput('');

    // Simulate smart bot response based on selected district
    setTimeout(() => {
      let botResponse = "";
      let showTable = false;
      let subtext = "";
      const lowerQuery = query.toLowerCase();

      if (lowerQuery.includes('priorit') && lowerQuery.includes('station')) {
        botResponse = "Based on AI analysis of demand, capacity gap, growth potential, and infrastructure readiness, the top priority districts for new charging stations are:";
        showTable = true;
        subtext = "These districts show high future demand and significant infrastructure gaps. Would you like me to show detailed insights for any of these districts?";
      } else if (lowerQuery.includes('hyderabad insights')) {
        botResponse = "Hyderabad is the highest priority district in Telangana with a priority score of 9.6/10. It has over 24,500 active EVs and a projected 2026 demand of 42 GWh. We recommend deploying 45x DC Ultra-Fast (150kW), 105x DC Fast (50kW), and 300x AC Type 2 (22kW) chargers in high-traffic zones like IT corridors and metro stations.";
      } else if (lowerQuery.includes('compare the top 3') || lowerQuery.includes('compare top 3')) {
        botResponse = "Comparing the top 3 priority districts:\n\n1. Hyderabad: Priority 9.6/10, EV Count: 24,500, 2026 Demand: 42 GWh, Recommended Stations: 450.\n2. Rangareddy: Priority 9.1/10, EV Count: 18,200, 2026 Demand: 36 GWh, Recommended Stations: 330.\n3. Medchal-Malkajgiri: Priority 8.8/10, EV Count: 12,800, 2026 Demand: 25 GWh, Recommended Stations: 230.\n\nAll three districts show critical capacity gaps and require immediate grid reinforcements and fast-charging deployments.";
      } else if (lowerQuery.includes('why is rangareddy critical')) {
        botResponse = "Rangareddy is classified as critical priority (score: 9.1/10) because of its massive EV adoption growth (currently 18,200 EVs) combined with its strategic location wrapping around Hyderabad. It contains major highway arterial routes like the Outer Ring Road (ORR) and transit plazas, where high-power fast charging is essential to support commuter and logistics traffic.";
      } else if (lowerQuery.includes('highest demand')) {
        botResponse = "According to our demand models, the districts with the highest projected EV demand in 2026 are Hyderabad (42 GWh), Rangareddy (36 GWh), and Medchal-Malkajgiri (25 GWh). Together, these three districts account for over 60% of the state's total charging demand.";
      } else if (lowerQuery.includes('capacity gap')) {
        botResponse = "The districts with the highest grid capacity gaps are Hyderabad (0.18 GWh shortage), Rangareddy (0.12 GWh shortage), and Medchal-Malkajgiri (0.08 GWh shortage). We recommend reinforcing substation grids in these areas before Q3 2025 to avoid peak load overruns.";
      } else if (lowerQuery.includes('low coverage') || lowerQuery.includes('areas have low coverage')) {
        botResponse = "Low coverage zones are primarily rural and peripheral districts such as Adilabad, Komaram Bheem, and Narayanpet. Although their current EV demand is low, establishing basic AC charging corridors is recommended to support inter-district travel connectivity.";
      } else if (lowerQuery.includes('priority') || lowerQuery.includes('score')) {
        botResponse = `The priority score for ${selectedDistrict} is currently ${activeData.priorityScore}/10. ${activeData.details} Its feasibility score is ${activeData.feasibility}.`;
      } else if (lowerQuery.includes('forecast') || lowerQuery.includes('future') || lowerQuery.includes('demand') || lowerQuery.includes('2030')) {
        botResponse = `Based on our machine learning models, EV charging demand in ${selectedDistrict} is projected to grow from ${activeData.demand2026} MWh in 2026 to ${activeData.demand2030} MWh by 2030. This represents a significant upward trend that warrants rapid infrastructure deployment.`;
      } else if (lowerQuery.includes('recommend') || lowerQuery.includes('place') || lowerQuery.includes('charger') || lowerQuery.includes('station')) {
        const recDetails = activeData.recs.map(r => `${r.count}x ${r.type} near ${r.area}`).join(', ');
        botResponse = `For ${selectedDistrict}, we recommend installing: ${recDetails}. Feasibility score is estimated at ${activeData.feasibility} based on grid capacity and road network metrics.`;
      } else {
        botResponse = `${selectedDistrict} currently has around ${activeData.evCount.toLocaleString()} active EVs. Our models recommend prioritizing ${activeData.recs[0]?.type || 'charging facilities'} in high-density sectors. Let me know if you would like details on priority scores, feasibility, or charging recommendations!`;
      }

      setChatHistory(prev => [...prev, { sender: 'bot', text: botResponse, timestamp: formattedTime, showTable, subtext }]);
    }, 600);
  };

  // Helper to color markers based on priority score
  const getPriorityColor = (level) => {
    switch (level) {
      case 'critical': return '#ef4444'; // Red
      case 'high': return '#f97316';     // Orange
      case 'medium': return '#fbbf24';   // Yellow
      case 'low': return '#10b981';      // Green
      default: return '#15803d';
    }
  };

  // Sidebar navigation items
  const NAV_ITEMS = [
    { id: 'dashboard', icon: LayoutDashboard, label: "Dashboard" },
    { id: 'explorer', icon: Map, label: "District Explorer" },
    { id: 'predictions', icon: TrendingUp, label: "Predictions" },
    { id: 'analytics', icon: BarChart2, label: "Analytics" },
    { id: 'assistant', icon: Bot, label: "AI Assistant" },
  ];

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
          className="flex h-screen bg-slate-50 overflow-hidden"
          style={{ fontFamily: "'Inter', system-ui, sans-serif" }}
        >
          {/* Dashboard Sidebar */}
          <aside
            className="flex-shrink-0 bg-white border-r border-slate-100 flex flex-col transition-all duration-300 ease-in-out py-4 px-3"
            style={{ width: sidebarCollapsed ? 76 : 260 }}
          >
            {/* Logo */}
            <div className="h-16 flex items-center px-2 gap-3 overflow-hidden mb-6 border-b border-slate-100 pb-4">
              <div className="w-9 h-9 rounded-xl bg-emerald-700 flex items-center justify-center flex-shrink-0 shadow-sm">
                <Zap className="w-5 h-5 text-white" />
              </div>
              {!sidebarCollapsed && (
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-bold text-slate-900 leading-tight">EVision</p>
                  <p className="text-xs text-emerald-700 font-semibold leading-tight mt-0.5">Telangana</p>
                </div>
              )}
              <button
                onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
                className={`p-1.5 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-slate-600 transition-colors flex-shrink-0 ${sidebarCollapsed ? "mx-auto" : ""}`}
              >
                {sidebarCollapsed ? <ChevronRight className="w-4 h-4" /> : <ChevronLeft className="w-4 h-4" />}
              </button>
            </div>

            {/* Nav */}
            <nav className="flex-1 space-y-1 overflow-hidden">
              {NAV_ITEMS.map((item) => {
                const Icon = item.icon;
                const active = dbTab === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => setDbTab(item.id)}
                    title={sidebarCollapsed ? item.label : undefined}
                    className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all group whitespace-nowrap overflow-hidden ${
                      active
                        ? "bg-emerald-50 text-emerald-800"
                        : "text-slate-500 hover:bg-slate-50 hover:text-slate-800"
                    } ${sidebarCollapsed ? "justify-center" : ""}`}
                  >
                    <Icon
                      className={`w-4 h-4 flex-shrink-0 ${
                        active ? "text-emerald-700" : "text-slate-400 group-hover:text-slate-600"
                      }`}
                    />
                    {!sidebarCollapsed && <span className="truncate">{item.label}</span>}
                    {!sidebarCollapsed && active && (
                      <span className="ml-auto w-1.5 h-1.5 rounded-full bg-emerald-700 flex-shrink-0" />
                    )}
                  </button>
                );
              })}
            </nav>

            {/* Sidebar Footer */}
            <div className="pt-4 border-t border-slate-100">
              <button
                onClick={() => setView('landing')}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-slate-500 hover:bg-emerald-50 hover:text-emerald-700 transition-all group ${
                  sidebarCollapsed ? "justify-center" : ""
                }`}
                title={sidebarCollapsed ? "Back to Landing Page" : undefined}
              >
                <ArrowLeft className="w-4 h-4 flex-shrink-0 text-slate-400 group-hover:text-emerald-700 transition-colors" />
                {!sidebarCollapsed && <span className="truncate font-semibold">Back to Landing</span>}
              </button>
            </div>
          </aside>

          {/* Main Window */}
          <div className="flex-1 flex flex-col min-w-0">
            {/* TopBar */}
            <header className="h-16 bg-white border-b border-slate-100 flex items-center px-6 gap-4 flex-shrink-0 justify-between">
              <div>
                <h1 className="text-base font-bold text-slate-900 leading-tight">
                  {NAV_ITEMS.find(n => n.id === dbTab)?.label || "Dashboard"}
                </h1>
                <p className="text-xs text-slate-400 leading-tight mt-0.5">
                  Telangana EV Infrastructure Planning
                </p>
              </div>

              {/* Centered wide search */}
              <div className="hidden md:flex flex-1 justify-center max-w-lg px-4">
                <div className="relative w-full">
                  <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                  <input
                    placeholder="Search districts, metrics, reports..."
                    className="w-full pl-11 pr-4 py-2 text-sm bg-slate-50 border border-slate-200 rounded-xl outline-none focus:ring-2 focus:ring-emerald-100 focus:border-emerald-700 transition-all placeholder:text-slate-400 text-slate-700"
                  />
                </div>
              </div>

              {/* District Dropdown Selector */}
              <div className="flex items-center gap-3">
                <span className="text-xs font-semibold text-slate-400">Active District:</span>
                <select
                  value={selectedDistrict}
                  onChange={(e) => setSelectedDistrict(e.target.value)}
                  className="bg-white text-slate-700 border border-slate-200 px-3 py-1.5 rounded-xl text-sm font-semibold outline-none focus:border-emerald-700 cursor-pointer shadow-sm"
                >
                  {Object.keys(districtData).sort().map(d => (
                    <option key={d} value={d}>{d}</option>
                  ))}
                </select>
              </div>
            </header>

            {/* Dashboard Content Area */}
            <main className="flex-1 overflow-y-auto p-5 box-border">
              {dbTab === 'dashboard' && (
                <div className="flex flex-col gap-4 h-full min-h-[500px]">
                  {/* KPI Cards Row */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    {[
                      {
                        title: "Total Districts",
                        value: "33",
                        icon: MapPin,
                        iconBg: "bg-emerald-50",
                        iconColor: "text-emerald-700",
                        borderClass: "border-emerald-100",
                      },
                      {
                        title: "Charging Stations",
                        value: districtsList.reduce((acc, d) => acc + d.recs.reduce((rAcc, r) => rAcc + r.count, 0), 0),
                        icon: Zap,
                        iconBg: "bg-amber-50",
                        iconColor: "text-amber-600",
                        borderClass: "border-amber-100",
                      },
                      {
                        title: "Predicted Demand",
                        value: (districtsList.reduce((acc, d) => acc + d.demand2030, 0) / 1000).toFixed(2) + " GWh",
                        icon: Activity,
                        iconBg: "bg-purple-50",
                        iconColor: "text-purple-600",
                        borderClass: "border-purple-100",
                      },
                      {
                        title: "High Priority Districts",
                        value: districtsList.filter(d => d.priorityLevel === 'critical' || d.priorityLevel === 'high').length,
                        icon: AlertTriangle,
                        iconBg: "bg-red-50",
                        iconColor: "text-red-600",
                        borderClass: "border-red-100",
                      },
                    ].map((card, i) => {
                      const Icon = card.icon;
                      return (
                        <div
                          key={i}
                          className={`bg-white rounded-2xl border ${card.borderClass} shadow-sm p-4 relative overflow-hidden transition-all duration-200`}
                        >
                          <div className="flex items-start justify-between mb-2">
                            <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                              {card.title}
                            </p>
                            <div className={`p-1.5 rounded-xl ${card.iconBg}`}>
                              <Icon className={`w-4 h-4 ${card.iconColor}`} />
                            </div>
                          </div>
                          <p className="text-2xl font-bold text-slate-950 tracking-tight">
                            {card.value}
                          </p>
                        </div>
                      );
                    })}
                  </div>

                  {/* Main row: map left, forecast + AI insights right */}
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 flex-1">
                    {/* Leaflet map styled as heatmap */}
                    <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden flex flex-col min-h-[350px]">
                      <div className="flex items-center justify-between px-5 py-3 border-b border-slate-100 flex-shrink-0">
                        <div>
                          <h2 className="text-sm font-semibold text-slate-900">District Priority Heatmap</h2>
                          <p className="text-xs text-slate-400 mt-0.5">Telangana · 33 Districts · Interactive Leaflet Map</p>
                        </div>
                      </div>
                      <div className="relative flex-1 bg-slate-50 min-h-[300px]">
                        <MapContainer 
                          center={[17.9784, 79.5941]} 
                          zoom={7.2} 
                          style={{ height: '100%', width: '100%' }}
                          zoomControl={true}
                        >
                          <TileLayer
                            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
                            url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
                          />
                          
                          {geojsonData ? (
                            <GeoJSON 
                              key={selectedDistrict + "_geojson_dash"}
                              data={geojsonData} 
                              style={styleDistrictFeature} 
                              onEachFeature={onEachDistrictFeature} 
                            />
                          ) : (
                            districtsList.map((d) => (
                              <CircleMarker
                                  key={d.name}
                                  center={d.coordinates}
                                  radius={d.name === selectedDistrict ? 22 : 14}
                                  fillColor={getPriorityColor(d.priorityLevel)}
                                  color={d.name === selectedDistrict ? '#ffffff' : getPriorityColor(d.priorityLevel)}
                                  weight={d.name === selectedDistrict ? 3.5 : 1}
                                  opacity={0.85}
                                  fillOpacity={0.65}
                                  eventHandlers={{
                                    click: () => {
                                      setSelectedDistrict(d.name);
                                    },
                                  }}
                                />
                            ))
                          )}

                          <ChangeView center={activeData.coordinates} />
                        </MapContainer>

                        {/* Legend Overlay */}
                        <div className="absolute bottom-3 left-3 bg-white/95 backdrop-blur-sm border border-slate-100 rounded-xl p-2.5 text-[9px] font-semibold text-slate-655 shadow-md z-[999] flex flex-col gap-2 min-w-[90px]">
                          <div className="flex items-center gap-2">
                            <span className="w-2.5 h-2.5 bg-[#ef4444] rounded-full inline-block" />
                            <span>Critical</span>
                          </div>
                          <div className="flex items-center gap-2">
                            <span className="w-2.5 h-2.5 bg-[#f97316] rounded-full inline-block" />
                            <span>High</span>
                          </div>
                          <div className="flex items-center gap-2">
                            <span className="w-2.5 h-2.5 bg-[#fbbf24] rounded-full inline-block" />
                            <span>Medium</span>
                          </div>
                          <div className="flex items-center gap-2">
                            <span className="w-2.5 h-2.5 bg-[#10b981] rounded-full inline-block" />
                            <span>Low</span>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Right column: demand forecast top, AI insights bottom */}
                    <div className="flex flex-col gap-4">
                      {/* AreaChart demand forecast trend */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col flex-1 min-h-[220px]">
                        <div className="flex items-center justify-between mb-4 flex-shrink-0">
                          <div>
                            <h2 className="text-sm font-semibold text-slate-900">Demand Forecast Trend ({selectedDistrict})</h2>
                            <p className="text-xs text-slate-400 mt-0.5">Actual vs AI-predicted · GWh</p>
                          </div>
                          <div className="flex items-center gap-4">
                            <div className="flex items-center gap-1.5">
                              <span className="w-4 h-0.5 bg-emerald-700 rounded-full inline-block" />
                              <span className="text-xs text-slate-500 font-medium">Actual</span>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <span className="w-4 h-0.5 border-t-2 border-dashed border-[#064e3b] inline-block" />
                              <span className="text-xs text-slate-500 font-medium">Forecast</span>
                            </div>
                          </div>
                        </div>
                        <div className="flex-1 min-h-[140px]">
                          <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={getAreaChartData()} margin={{ top: 4, right: 4, bottom: 0, left: -22 }}>
                              <defs>
                                <linearGradient id="gradActual" x1="0" y1="0" x2="0" y2="1">
                                  <stop offset="5%"  stopColor="#047857" stopOpacity={0.18} />
                                  <stop offset="95%" stopColor="#047857" stopOpacity={0} />
                                </linearGradient>
                                <linearGradient id="gradForecast" x1="0" y1="0" x2="0" y2="1">
                                  <stop offset="5%"  stopColor="#064e3b" stopOpacity={0.1} />
                                  <stop offset="95%" stopColor="#064e3b" stopOpacity={0} />
                                </linearGradient>
                              </defs>
                              <CartesianGrid strokeDasharray="3 3" stroke="#F1F5F9" vertical={false} />
                              <XAxis
                                dataKey="month"
                                tick={{ fontSize: 10, fill: "#94A3B8", fontFamily: "Inter" }}
                                axisLine={false}
                                tickLine={false}
                              />
                              <YAxis
                                tick={{ fontSize: 10, fill: "#94A3B8", fontFamily: "Inter" }}
                                axisLine={false}
                                tickLine={false}
                                domain={['auto', 'auto']}
                              />
                              <Tooltip content={({ active, payload, label }) => {
                                if (!active || !payload?.length) return null;
                                return (
                                  <div className="bg-white border border-slate-200 rounded-xl shadow-lg p-3 text-xs">
                                    <p className="font-bold text-slate-700 mb-2">{label}</p>
                                    {payload.map((p, i) => (
                                      p.value != null && (
                                        <div key={i} className="flex items-center gap-2 mb-1 last:mb-0">
                                          <span className="w-2 h-2 rounded-full flex-shrink-0" style={{ background: p.color }} />
                                          <span className="text-slate-500">{p.name}:</span>
                                          <span className="font-bold text-slate-900">{p.value} GWh</span>
                                        </div>
                                      )
                                    ))}
                                  </div>
                                );
                              }} />
                              <Area
                                type="monotone"
                                dataKey="actual"
                                stroke="#047857"
                                strokeWidth={2.5}
                                fill="url(#gradActual)"
                                name="Actual"
                                dot={false}
                                  activeDot={{ r: 4, fill: "#047857", strokeWidth: 0 }}
                              />
                              <Area
                                type="monotone"
                                dataKey="forecast"
                                stroke="#064e3b"
                                strokeWidth={2}
                                strokeDasharray="5 4"
                                fill="url(#gradForecast)"
                                name="Forecast"
                                dot={false}
                                activeDot={{ r: 4, fill: "#064e3b", strokeWidth: 0 }}
                              />
                            </AreaChart>
                          </ResponsiveContainer>
                        </div>
                      </div>

                      {/* AI Insights Card */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col h-[180px] flex-shrink-0 justify-between">
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-emerald-600 to-teal-500 flex items-center justify-center flex-shrink-0 shadow-sm">
                            <Sparkles className="w-4 h-4 text-white" />
                          </div>
                          <div>
                            <p className="text-sm font-semibold text-slate-900 leading-tight">AI Insights</p>
                            <p className="text-[11px] text-slate-400 leading-tight">Statewide Analysis Summary</p>
                          </div>
                          <button
                            onClick={() => setDbTab('assistant')}
                            className="ml-auto px-2.5 py-1.5 text-xs font-semibold text-emerald-800 bg-emerald-50 rounded-xl hover:bg-emerald-100 transition-colors flex items-center gap-1.5 whitespace-nowrap"
                          >
                            <Bot className="w-3.5 h-3.5" />
                            Open Assistant
                          </button>
                        </div>
                        <div className="border-t border-slate-100 pt-3 flex-1 flex flex-col justify-between">
                          <p className="text-xs text-slate-600 leading-relaxed">
                            <span className="font-semibold text-slate-900">Hyderabad, Rangareddy &amp; Medchal-Malkajgiri</span> are flagged as Critical zones. Priority scored at {activeData.priorityScore}/10 for {selectedDistrict}. Strong demand correlates with urbanization.
                          </p>
                          <div className="grid grid-cols-3 gap-2 mt-2">
                            {[
                              { label: "High Risk Zones", val: "10 districts", color: "text-red-600", bg: "bg-red-50" },
                              { label: "State Capacity", val: "412 stations", color: "text-amber-700", bg: "bg-amber-50" },
                              { label: "ML Projects", val: "Demand up 2.4x", color: "text-emerald-700", bg: "bg-emerald-50" },
                            ].map((insight, i) => (
                              <div key={i} className={`rounded-xl px-2 py-1.5 text-center ${insight.bg}`}>
                                <p className="text-[9px] text-slate-500 mb-0.5 leading-none">{insight.label}</p>
                                <p className={`text-xs font-bold ${insight.color}`}>{insight.val}</p>
                              </div>
                            ))}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {dbTab === 'explorer' && (() => {
                const scale = activeData.evCount / 24500;
                const populationVal = activeData.name === "Hyderabad" ? "10.1 Million" : activeData.name === "Rangareddy" ? "5.3 Million" : activeData.name === "Medchal-Malkajgiri" ? "4.0 Million" : (scale * 8 + 1).toFixed(1) + " Million";
                const areaVal = activeData.name === "Hyderabad" ? "217.3 km²" : activeData.name === "Rangareddy" ? "7,493 km²" : activeData.name === "Medchal-Malkajgiri" ? "1,084 km²" : (scale * 6000 + 800).toLocaleString() + " km²";
                const urbanizationVal = activeData.name === "Hyderabad" ? "100%" : activeData.name === "Rangareddy" ? "78%" : activeData.name === "Medchal-Malkajgiri" ? "91%" : Math.round(activeData.priorityScore * 8 + 10) + "%";
                const roadDensityVal = activeData.name === "Hyderabad" ? "12.4 km/km²" : activeData.name === "Rangareddy" ? "4.8 km/km²" : (activeData.priorityScore * 1.1 + 0.5).toFixed(1) + " km/km²";
                const existingStationsVal = Math.round(activeData.evCount * 0.00196);
                const fastChargersVal = Math.round(activeData.evCount * 0.00065);

                const currentDemandVal = (activeData.demand2026 * 0.025).toFixed(2);
                const predictedDemandVal = (activeData.demand2026 * 0.0305).toFixed(2);
                const growthRateVal = "+" + (((activeData.demand2028 - activeData.demand2026)/activeData.demand2026)*19.5).toFixed(1) + "%";
                const chargingCapacityVal = (activeData.demand2026 * 0.0171).toFixed(2);
                const capacityGapVal = (activeData.demand2026 * 0.0133).toFixed(2);
                const utilizationRateVal = Math.round(activeData.priorityScore * 6 + 10);

                const riskScoreVal = Math.round(activeData.priorityScore * 7.5 + 6);
                const riskLevelVal = riskScoreVal >= 75 ? "High Risk" : riskScoreVal >= 50 ? "Medium Risk" : "Low Risk";

                const lat = activeData.coordinates[0];
                const lng = activeData.coordinates[1];
                const mockSites = [
                  { lat: lat + 0.012, lng: lng - 0.015, type: "existing", label: "Metro Parking Charger" },
                  { lat: lat - 0.008, lng: lng + 0.018, type: "existing", label: "Public Mall AC Hub" },
                  { lat: lat + 0.018, lng: lng + 0.008, type: "proposed", label: "Hitec City Fast DC" },
                  { lat: lat - 0.015, lng: lng - 0.01, type: "proposed", label: "Tourist Park Charging" },
                  { lat: lat + 0.004, lng: lng + 0.004, type: "high_power", label: "Highway DC Superfast" },
                  { lat: lat - 0.004, lng: lng - 0.018, type: "existing", label: "Commercial Hub AC" },
                  { lat: lat + 0.022, lng: lng - 0.022, type: "proposed", label: "Bypass Charging Station" },
                  { lat: lat - 0.022, lng: lng + 0.022, type: "high_power", label: "Ring Road Station" },
                ];

                return (
                  <div className="space-y-4 flex flex-col h-[calc(100vh-105px)] min-h-0">
                    {/* Header */}
                    <div className="flex flex-col xl:flex-row xl:items-center justify-between pb-2.5 border-b border-slate-100 gap-4 flex-shrink-0">
                      <div>
                        <h2 className="text-xl font-bold text-slate-900 leading-tight">District Explorer</h2>
                        <p className="text-xs text-slate-400 mt-1 font-medium">Explore district-level EV infrastructure and demand insights</p>
                      </div>
                      <div className="flex flex-wrap items-center gap-3">
                        <button className="flex items-center gap-2 px-3 py-2 bg-emerald-50 text-emerald-800 rounded-xl hover:bg-emerald-100 transition-colors text-xs font-semibold shadow-sm cursor-pointer border-0">
                          <Download className="w-3.5 h-3.5" />
                          <span>Export Report</span>
                        </button>
                      </div>
                    </div>

                    {/* Cards Row (District Info, EV Stats, Risk Score) */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 flex-shrink-0 h-[178px]">
                      {/* District Information (span 4) */}
                      <div className="lg:col-span-4 bg-white rounded-2xl border border-slate-100 shadow-sm p-3.5 py-3 flex flex-col justify-between h-full">
                        <div className="flex items-center justify-between pb-1.5 border-b border-slate-50">
                          <h4 className="text-[11px] font-bold text-slate-900 uppercase tracking-wider">District Information</h4>
                          <ShieldCheck className="w-3.5 h-3.5 text-emerald-700 bg-emerald-50 rounded p-0.5" />
                        </div>
                        
                        <div className="space-y-1 mt-2 text-[11px] font-semibold text-slate-500">
                          {[
                            { label: "Population", val: populationVal, icon: Bot },
                            { label: "Area", val: areaVal, icon: Map },
                            { label: "Urbanization", val: urbanizationVal, icon: Layers },
                            { label: "Road Density", val: roadDensityVal, icon: Target },
                            { label: "Existing Stations", val: existingStationsVal, icon: Zap },
                            { label: "Fast Chargers", val: fastChargersVal, icon: Zap }
                          ].map((item, i) => {
                            const Icon = item.icon;
                            return (
                              <div key={i} className="flex justify-between items-center py-0.5">
                                <div className="flex items-center gap-1.5">
                                  <Icon className="w-3 h-3 text-slate-400" />
                                  <span>{item.label}</span>
                                </div>
                                <span className="font-bold text-slate-800">{item.val}</span>
                              </div>
                            );
                          })}
                        </div>
                      </div>

                      {/* EV Infrastructure & Demand (span 5) */}
                      <div className="lg:col-span-5 bg-white rounded-2xl border border-slate-100 shadow-sm p-3.5 py-3 flex flex-col justify-between h-full">
                        <div className="flex items-center justify-between pb-1.5 border-b border-slate-50">
                          <h4 className="text-[11px] font-bold text-slate-900 uppercase tracking-wider">EV Infrastructure &amp; Demand</h4>
                          <Zap className="w-3.5 h-3.5 text-emerald-700 bg-emerald-50 rounded p-0.5" />
                        </div>
                        
                        <div className="space-y-1.5 mt-2 text-[11px] font-semibold text-slate-500">
                          <div className="flex justify-between items-center py-0.2">
                            <span className="flex items-center gap-1.5"><MapPin className="w-3 h-3 text-slate-400" />Current EV Demand (Monthly)</span>
                            <span className="font-bold text-slate-800">{currentDemandVal} GWh</span>
                          </div>
                          <div className="flex justify-between items-center py-0.2">
                            <span className="flex items-center gap-1.5"><TrendingUp className="w-3 h-3 text-slate-400" />Predicted Demand (FY2025)</span>
                            <span className="font-bold text-slate-800">{predictedDemandVal} GWh</span>
                          </div>
                          <div className="flex justify-between items-center py-0.2">
                            <span className="flex items-center gap-1.5"><Activity className="w-3 h-3 text-slate-400" />Growth Rate (YoY)</span>
                            <span className="font-bold text-emerald-700">{growthRateVal} ↑</span>
                          </div>
                          <div className="flex justify-between items-center py-0.2">
                            <span className="flex items-center gap-1.5"><Zap className="w-3 h-3 text-slate-400" />Charging Capacity</span>
                            <span className="font-bold text-slate-800">{chargingCapacityVal} GWh</span>
                          </div>
                          <div className="flex justify-between items-center py-0.2">
                            <span className="flex items-center gap-1.5"><AlertTriangle className="w-3 h-3 text-slate-400" />Capacity Gap</span>
                            <span className="font-bold text-orange-655">{capacityGapVal} GWh</span>
                          </div>
                          
                          {/* Utilization Rate Progress bar */}
                          <div className="flex justify-between items-center pt-1 border-t border-slate-50">
                            <span className="flex items-center gap-1.5"><Clock className="w-3 h-3 text-slate-400" />Utilization Rate</span>
                            <div className="flex items-center gap-2.5 w-32">
                              <div className="flex-grow h-1.5 bg-slate-50 border border-slate-100 rounded-full overflow-hidden">
                                <div className="h-full bg-emerald-700 rounded-full" style={{ width: `${utilizationRateVal}%` }} />
                              </div>
                              <span className="font-bold text-slate-850 w-6 text-right text-[10px]">{utilizationRateVal}%</span>
                            </div>
                          </div>
                        </div>
                      </div>

                      {/* District Risk Score (span 3) */}
                      <div className="lg:col-span-3 bg-white rounded-2xl border border-slate-100 shadow-sm p-3.5 py-3 flex flex-col justify-between h-full">
                        <div className="flex items-center justify-between pb-1.5 border-b border-slate-50">
                          <h4 className="text-[11px] font-bold text-slate-900 uppercase tracking-wider">District Risk Score</h4>
                          <ShieldCheck className="w-3.5 h-3.5 text-emerald-700 bg-emerald-50 rounded p-0.5" />
                        </div>
                        
                        <div className="my-auto flex flex-col items-center justify-center pt-1">
                          <div className="relative w-36 h-18 flex items-end justify-center">
                            <svg className="w-full h-full" viewBox="0 0 100 50">
                              <defs>
                                <linearGradient id="riskGradient" x1="0" y1="0" x2="1" y2="0">
                                  <stop offset="0%" stopColor="#22c55e" />
                                  <stop offset="50%" stopColor="#eab308" />
                                  <stop offset="100%" stopColor="#ef4444" />
                                </linearGradient>
                              </defs>
                              <path
                                d="M 10 50 A 40 40 0 0 1 90 50"
                                fill="none"
                                stroke="#f8fafc"
                                strokeWidth="8"
                                strokeLinecap="round"
                              />
                              <path
                                d="M 10 50 A 40 40 0 0 1 90 50"
                                fill="none"
                                stroke="url(#riskGradient)"
                                strokeWidth="8"
                                strokeLinecap="round"
                                strokeDasharray="125.6"
                                strokeDashoffset={125.6 * (1 - riskScoreVal / 100)}
                              />
                            </svg>
                            <div className="absolute inset-0 flex flex-col items-center justify-end pb-0.5">
                              <span className="text-xl font-extrabold text-slate-900 tracking-tight">{riskScoreVal}<span className="text-[9px] font-normal text-slate-400">/100</span></span>
                              <span className={`text-[8px] font-bold mt-0.5 uppercase tracking-wide ${riskScoreVal >= 75 ? 'text-red-500' : riskScoreVal >= 50 ? 'text-orange-500' : 'text-emerald-750'}`}>
                                {riskLevelVal}
                              </span>
                            </div>
                          </div>
                        </div>
                        <p className="text-[9.5px] text-slate-400 font-semibold text-center mt-2 leading-tight">
                          High demand pressure and infrastructure gap indicate urgent attention.
                        </p>
                      </div>
                    </div>

                    {/* Bottom Row: Map and AI Recommendations */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 flex-1 min-h-0">
                      {/* Left: Map & Infrastructure Overview (span 7) */}
                      <div className="lg:col-span-7 bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col h-full min-h-0">
                        <div className="flex justify-between items-center flex-shrink-0 pb-1.5">
                          <div>
                            <h4 className="text-xs font-bold text-slate-900 leading-tight">District Priority Heatmap</h4>
                            <p className="text-[10px] text-slate-400 mt-0.5 font-medium leading-none">AI-Scored priority levels across Telangana</p>
                          </div>
                          <button className="flex items-center gap-1 px-2.5 py-1 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 transition-colors rounded-lg text-[10px] font-bold shadow-sm cursor-pointer">
                            <Download className="w-3.5 h-3.5 text-slate-400" />
                            <span>Export Map</span>
                          </button>
                        </div>
                        
                        <div className="flex-1 bg-slate-55 border border-slate-100 rounded-2xl overflow-hidden relative my-2 min-h-0">
                          <MapContainer 
                            center={[17.9784, 79.5941]} 
                            zoom={7.2} 
                            style={{ height: '100%', width: '100%' }}
                            zoomControl={true}
                          >
                            <TileLayer
                              url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
                            />
                            
                            {geojsonData ? (
                              <GeoJSON 
                                key={selectedDistrict + "_geojson"}
                                data={geojsonData} 
                                style={styleDistrictFeature} 
                                onEachFeature={onEachDistrictFeature} 
                              />
                            ) : (
                              districtsList.map((d) => (
                                <CircleMarker
                                  key={d.name}
                                  center={d.coordinates}
                                  radius={d.name === selectedDistrict ? 22 : 14}
                                  fillColor={getPriorityColor(d.priorityLevel)}
                                  color={d.name === selectedDistrict ? '#ffffff' : getPriorityColor(d.priorityLevel)}
                                  weight={d.name === selectedDistrict ? 3.5 : 1}
                                  opacity={0.85}
                                  fillOpacity={0.65}
                                  eventHandlers={{
                                    click: () => {
                                      setSelectedDistrict(d.name);
                                    },
                                  }}
                                />
                              ))
                            )}

                            <ChangeView center={activeData.coordinates} />
                          </MapContainer>

                          {/* Legend Overlay */}
                          <div className="absolute bottom-3 left-3 bg-white/95 backdrop-blur-sm border border-slate-100 rounded-xl p-2.5 text-[9px] font-semibold text-slate-655 shadow-md z-[999] flex flex-col gap-2 min-w-[90px]">
                            <div className="flex items-center gap-2">
                              <span className="w-2.5 h-2.5 bg-[#ef4444] rounded-full inline-block" />
                              <span>Critical</span>
                            </div>
                            <div className="flex items-center gap-2">
                              <span className="w-2.5 h-2.5 bg-[#f97316] rounded-full inline-block" />
                              <span>High</span>
                            </div>
                            <div className="flex items-center gap-2">
                              <span className="w-2.5 h-2.5 bg-[#fbbf24] rounded-full inline-block" />
                              <span>Medium</span>
                            </div>
                            <div className="flex items-center gap-2">
                              <span className="w-2.5 h-2.5 bg-[#10b981] rounded-full inline-block" />
                              <span>Low</span>
                            </div>
                          </div>
                        </div>

                        <p className="text-[9.5px] text-slate-400 font-semibold flex items-center gap-1 flex-shrink-0">
                          <ShieldCheck className="w-3.5 h-3.5 text-slate-450" />
                          <span>Click on any district on the map to inspect its information, risk score, and demand insights.</span>
                        </p>
                      </div>

                      {/* Right: AI Recommendations (span 5) */}
                      <div className="lg:col-span-5 bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col h-full min-h-0 justify-between">
                        <div className="flex-shrink-0">
                          <h4 className="text-xs font-bold text-slate-900 leading-tight">AI Recommendations</h4>
                          <p className="text-[10px] text-slate-400 mt-0.5 font-medium leading-none">Priority actions for {activeData.name}</p>
                        </div>
                        
                        {/* Recommendations Scrollable List */}
                        <div className="flex-1 overflow-y-auto space-y-2 my-2.5 pr-1 min-h-0">
                          {/* Rec Card 1 */}
                          <div className="bg-slate-50/50 border border-slate-100 hover:border-emerald-100 rounded-xl p-2.5 flex justify-between items-center transition-all group">
                            <div className="flex gap-2.5 items-center min-w-0">
                              <div className="p-1.5 rounded-lg bg-emerald-50 text-emerald-700 flex-shrink-0 group-hover:bg-emerald-100/70">
                                <Zap className="w-3.5 h-3.5" />
                              </div>
                              <div className="min-w-0">
                                <p className="text-[11px] font-bold text-slate-800 leading-tight">Increase Fast Charging Stations</p>
                                <p className="text-[9.5px] text-slate-450 mt-0.5 leading-normal">Add {Math.round(activeData.evCount * 0.00098)} more fast chargers to meet rising demand in high-traffic zones.</p>
                              </div>
                            </div>
                            <span className="text-[8px] font-bold uppercase tracking-wider text-emerald-800 bg-emerald-50/80 px-1.5 py-0.5 rounded flex-shrink-0 ml-2">High Priority</span>
                          </div>

                          {/* Rec Card 2 */}
                          <div className="bg-slate-50/50 border border-slate-100 hover:border-orange-100 rounded-xl p-2.5 flex justify-between items-center transition-all group">
                            <div className="flex gap-2.5 items-center min-w-0">
                              <div className="p-1.5 rounded-lg bg-orange-50 text-orange-600 flex-shrink-0 group-hover:bg-orange-100/70">
                                <Compass className="w-3.5 h-3.5" />
                              </div>
                              <div className="min-w-0">
                                <p className="text-[11px] font-bold text-slate-800 leading-tight">Expand Along Highway Corridors</p>
                                <p className="text-[9.5px] text-slate-450 mt-0.5 leading-normal">Develop charging hubs along ORR and NH44 for inter-city connectivity.</p>
                              </div>
                            </div>
                            <span className="text-[8px] font-bold uppercase tracking-wider text-orange-655 bg-orange-50/80 px-1.5 py-0.5 rounded flex-shrink-0 ml-2">Medium Priority</span>
                          </div>

                          {/* Rec Card 3 */}
                          <div className="bg-slate-50/50 border border-slate-100 hover:border-emerald-100 rounded-xl p-2.5 flex justify-between items-center transition-all group">
                            <div className="flex gap-2.5 items-center min-w-0">
                              <div className="p-1.5 rounded-lg bg-emerald-50 text-emerald-700 flex-shrink-0 group-hover:bg-emerald-100/70">
                                <Layers className="w-3.5 h-3.5" />
                              </div>
                              <div className="min-w-0">
                                <p className="text-[11px] font-bold text-slate-800 leading-tight">Strengthen Urban Coverage</p>
                                <p className="text-[9.5px] text-slate-450 mt-0.5 leading-normal">Improve station density in dense residential and commercial areas.</p>
                              </div>
                            </div>
                            <span className="text-[8px] font-bold uppercase tracking-wider text-orange-655 bg-orange-50/80 px-1.5 py-0.5 rounded flex-shrink-0 ml-2">Medium Priority</span>
                          </div>
                        </div>

                        {/* Additional Info row */}
                        <div className="bg-emerald-50/20 border border-emerald-100/40 rounded-xl p-3 flex flex-col justify-between gap-2.5 flex-shrink-0">
                          <div className="flex justify-between items-center text-xs">
                            <div>
                              <p className="text-[8.5px] font-bold text-slate-400 uppercase tracking-wider leading-none">Estimated Additional Investment</p>
                              <p className="text-base font-black text-emerald-800 mt-1.5 leading-none">₹ {activeData.name === "Hyderabad" ? "128" : Math.round(activeData.evCount * 0.0052)} Cr</p>
                            </div>
                            <div className="text-right">
                              <p className="text-[8.5px] font-bold text-slate-400 uppercase tracking-wider leading-none">Recommended Stations</p>
                              <p className="text-base font-black text-emerald-800 mt-1.5 leading-none">{Math.round(activeData.evCount * 0.00098)}</p>
                            </div>
                          </div>
                          
                          <p className="text-[9.5px] text-emerald-850 font-bold border-t border-emerald-100/50 pt-2 text-center">
                            Potential to meet 92% of future demand by FY2026
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                );
              })()}

              {dbTab === 'predictions' && (() => {
                const confidenceScore = selectedDistrict === 'Hyderabad' ? 92 : (activeData.priorityScore > 8 ? 94 : activeData.priorityScore > 7 ? 89 : 83);
                const features = [
                  { name: "Population Density", value: 28.7 },
                  { name: "EV Adoption Rate", value: 21.4 },
                  { name: "Urbanization Level", value: 16.8 },
                  { name: "Road Network Density", value: 12.3 },
                  { name: "Avg. Income Level", value: 8.9 },
                  { name: "Existing Station Density", value: 6.2 },
                  { name: "Traffic Volume Index", value: 5.7 },
                ];
                return (
                  <div className="space-y-6">
                    {/* Header */}
                    <div className="flex flex-col xl:flex-row xl:items-center justify-between pb-4 border-b border-slate-100 gap-4">
                      <div>
                        <h2 className="text-xl font-bold text-slate-900 leading-tight">AI Predictions</h2>
                        <p className="text-xs text-slate-400 mt-1">ML-powered demand forecasting and infrastructure predictions</p>
                      </div>
                      <div className="flex flex-wrap items-center gap-3">
                        <div className="flex items-center gap-2 px-3 py-2 bg-white border border-slate-200 rounded-xl shadow-sm text-xs font-semibold text-slate-700">
                          <Calendar className="w-3.5 h-3.5 text-slate-400" />
                          <span>Jan 2025 - Dec 2026</span>
                          <ChevronDown className="w-3.5 h-3.5 text-slate-400 ml-1" />
                        </div>
                        <button className="flex items-center gap-2 px-3 py-2 bg-emerald-50 text-emerald-800 rounded-xl hover:bg-emerald-100 transition-colors text-xs font-semibold shadow-sm cursor-pointer border-0">
                          <Download className="w-3.5 h-3.5" />
                          <span>Export Report</span>
                        </button>
                      </div>
                    </div>

                    {/* Cards Row (12 Columns Grid) */}
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-12 gap-4">
                      {/* Card 1: Predicted Demand (span 3) */}
                      <div className="lg:col-span-3 sm:col-span-1 bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[160px]">
                        <div className="flex items-start justify-between">
                          <div>
                            <h4 className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Predicted Demand</h4>
                            <p className="text-[9px] text-slate-400 font-semibold mt-0.5">Dec 2026 (Monthly)</p>
                          </div>
                          <div className="p-1.5 rounded-xl bg-emerald-50 text-emerald-700 flex-shrink-0">
                            <TrendingUp className="w-3.5 h-3.5" />
                          </div>
                        </div>
                        <div className="mt-2">
                          <p className="text-2xl font-extrabold text-slate-900 tracking-tight">
                            {(activeData.demand2026 * 0.0338).toFixed(2)} GWh
                          </p>
                          <p className="text-[9px] text-slate-455 font-semibold mt-1 leading-normal">
                            ± {(activeData.demand2026 * 0.0019).toFixed(2)} GWh (Confidence Interval)
                          </p>
                        </div>
                      </div>

                      {/* Card 2: Confidence Score (span 3) */}
                      <div className="lg:col-span-3 sm:col-span-1 bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[160px]">
                        <div className="flex items-start justify-between">
                          <div>
                            <h4 className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Confidence Score</h4>
                          </div>
                          <div className="p-1.5 rounded-xl bg-emerald-50 text-emerald-700 flex-shrink-0">
                            <ShieldCheck className="w-3.5 h-3.5" />
                          </div>
                        </div>
                        <div className="mt-2">
                          <p className="text-2xl font-extrabold text-slate-900 tracking-tight">
                            {confidenceScore}%
                          </p>
                          <p className="text-[11px] text-emerald-700 font-bold mt-1">
                            High Confidence
                          </p>
                        </div>
                      </div>

                      {/* Card 3: Expected Growth (span 3) */}
                      <div className="lg:col-span-3 sm:col-span-1 bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[160px]">
                        <div className="flex items-start justify-between">
                          <div>
                            <h4 className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Expected Growth (YoY)</h4>
                          </div>
                          <div className="p-1.5 rounded-xl bg-emerald-50 text-emerald-700 flex-shrink-0">
                            <Activity className="w-3.5 h-3.5" />
                          </div>
                        </div>
                        <div className="mt-2">
                          <p className="text-2xl font-extrabold text-emerald-750 tracking-tight font-black">
                            +{(((activeData.demand2028 - activeData.demand2026) / activeData.demand2026) * 22.3).toFixed(1)}% ↑
                          </p>
                          <p className="text-[9px] text-slate-400 font-semibold mt-1">
                            Compared to Dec 2025
                          </p>
                        </div>
                      </div>

                      {/* Card 4: Recommended Stations (span 3) */}
                      <div className="lg:col-span-3 sm:col-span-1 bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[160px]">
                        <div className="flex items-start justify-between">
                          <div>
                            <h4 className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Recommended Stations</h4>
                          </div>
                          <div className="p-1.5 rounded-xl bg-emerald-50 text-emerald-700 flex-shrink-0">
                            <Zap className="w-3.5 h-3.5" />
                          </div>
                        </div>
                        <div className="mt-2">
                          <p className="text-2xl font-extrabold text-slate-900 tracking-tight font-black">
                            {Math.round(activeData.evCount * 0.00098)}
                          </p>
                          <p className="text-[9px] text-slate-400 font-semibold mt-1">
                            Additional stations needed
                          </p>
                        </div>
                      </div>
                    </div>

                    {/* Charts Row */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-4">
                      {/* Demand Forecast Trend (span 8) */}
                      <div className="lg:col-span-8 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col min-h-[360px]">
                        <div className="flex items-center justify-between mb-4">
                          <div>
                            <h4 className="text-sm font-semibold text-slate-900">Demand Forecast Trend</h4>
                            <p className="text-xs text-slate-400 mt-0.5 font-medium">Historical vs AI-Predicted Demand · GWh</p>
                          </div>
                          <div className="flex items-center gap-4 text-xs font-semibold text-slate-500">
                            <div className="flex items-center gap-1.5">
                              <span className="w-3.5 h-0.5 bg-emerald-700 inline-block rounded-full animate-pulse" />
                              <span>Actual</span>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <span className="w-3.5 h-0.5 border-t border-dashed border-emerald-750 inline-block" />
                              <span>AI Forecast</span>
                            </div>
                          </div>
                        </div>
                        <div className="flex-1 min-h-[250px]">
                          <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={getForecastTrendData()} margin={{ top: 10, right: 10, left: -22, bottom: 0 }}>
                              <defs>
                                <linearGradient id="gradPredictions" x1="0" y1="0" x2="0" y2="1">
                                  <stop offset="5%" stopColor="#15803d" stopOpacity={0.15}/>
                                  <stop offset="95%" stopColor="#15803d" stopOpacity={0}/>
                                </linearGradient>
                              </defs>
                              <CartesianGrid strokeDasharray="3 3" stroke="#f8fafc" vertical={false} />
                              <XAxis 
                                dataKey="month" 
                                stroke="#94A3B8" 
                                fontSize={10} 
                                tickLine={false} 
                                axisLine={false}
                                tick={{ fill: "#94A3B8", fontFamily: "Inter" }}
                              />
                              <YAxis 
                                stroke="#94A3B8" 
                                fontSize={10} 
                                tickLine={false} 
                                axisLine={false}
                                tick={{ fill: "#94A3B8", fontFamily: "Inter" }}
                              />
                              <Tooltip 
                                contentStyle={{ backgroundColor: '#ffffff', borderColor: '#e2e8f0', borderRadius: '12px', color: '#0f172a', fontSize: '11px' }}
                                labelStyle={{ color: '#15803d', fontWeight: 'bold' }}
                                formatter={(val) => [`${val} GWh`, '']}
                              />
                              <Area 
                                type="monotone" 
                                dataKey="actual" 
                                stroke="#15803d" 
                                strokeWidth={2.5} 
                                fill="url(#gradPredictions)"
                                name="Actual"
                                dot={{ strokeWidth: 1.5, r: 2.5, fill: '#ffffff' }}
                                activeDot={{ r: 5 }} 
                              />
                              <Area 
                                type="monotone" 
                                dataKey="forecast" 
                                stroke="#15803d" 
                                strokeWidth={2.5} 
                                strokeDasharray="4 4"
                                fill="url(#gradPredictions)"
                                name="AI Forecast"
                                dot={false}
                                activeDot={{ r: 5 }} 
                              />
                            </AreaChart>
                          </ResponsiveContainer>
                        </div>
                      </div>

                      {/* Feature Importance (span 4) */}
                      <div className="lg:col-span-4 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col justify-between min-h-[360px]">
                        <div>
                          <h4 className="text-sm font-semibold text-slate-900">Feature Importance</h4>
                          <p className="text-xs text-slate-400 mt-0.5">Top factors driving predicted demand</p>
                        </div>
                        <div className="space-y-3.5 my-4 flex-1 flex flex-col justify-center">
                          {features.map((f, i) => (
                            <div key={i} className="flex items-center gap-3">
                              <span className="w-28 text-xs font-semibold text-slate-600 truncate leading-none">{f.name}</span>
                              <div className="flex-1 h-2 bg-slate-50 border border-slate-100 rounded-full overflow-hidden">
                                <div className="h-full bg-emerald-700 rounded-full transition-all duration-500" style={{ width: `${f.value}%` }} />
                              </div>
                              <span className="w-9 text-right text-[11px] font-bold text-slate-700 leading-none">{f.value}%</span>
                            </div>
                          ))}
                        </div>
                        <p className="text-[10px] text-slate-400 font-semibold border-t border-slate-50 pt-3">
                          Model uses 15 features for prediction
                        </p>
                      </div>
                    </div>

                    {/* Details Row */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-4">
                      {/* AI Prediction Explanation (span 8) */}
                      <div className="lg:col-span-8 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col justify-between min-h-[220px]">
                        <div>
                          <h4 className="text-sm font-semibold text-slate-900">AI Prediction Explanation</h4>
                          <p className="text-xs text-slate-400 mt-0.5">Why is demand expected to increase?</p>
                        </div>
                        <div className="my-3">
                          <div className="bg-emerald-50/40 border border-emerald-100/50 rounded-xl p-3 flex gap-2.5 items-start">
                            <Sparkles className="w-4 h-4 text-emerald-700 flex-shrink-0 mt-0.5 animate-pulse" />
                            <p className="text-[11px] text-slate-600 leading-relaxed">
                              <span className="font-semibold text-slate-900">{selectedDistrict}</span>'s EV demand is projected to increase mainly due to high population growth, <span className="font-semibold text-emerald-800">rising EV adoption rate</span>, improved road infrastructure, and government incentives. The current charging infrastructure is insufficient to meet future demand.
                            </p>
                          </div>
                        </div>
                        <div className="flex flex-wrap gap-2">
                          {[
                            "High population growth",
                            "Rising EV adoption",
                            "Infrastructure gap",
                            "Policy support"
                          ].map((item, i) => (
                            <div key={i} className="flex items-center gap-1 px-2 py-1 bg-emerald-50/70 border border-emerald-100/30 rounded-lg text-[10px] font-semibold text-emerald-800">
                              <Check className="w-3 h-3 text-emerald-700" />
                              <span>{item}</span>
                            </div>
                          ))}
                        </div>
                      </div>

                      {/* Prediction Details (span 4) */}
                      <div className="lg:col-span-4 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col justify-between min-h-[220px]">
                        <div>
                          <h4 className="text-sm font-semibold text-slate-900">Prediction Details</h4>
                        </div>
                        <div className="space-y-2.5 my-3 flex-1 flex flex-col justify-center text-xs">
                          <div className="flex justify-between items-center py-1 border-b border-slate-50">
                            <span className="text-slate-450 font-medium font-semibold">Model Used</span>
                            <span className="font-bold text-emerald-700">XGBoost Regressor</span>
                          </div>
                          <div className="flex justify-between items-center py-1 border-b border-slate-50">
                            <span className="text-slate-450 font-medium font-semibold">Training Data</span>
                            <span className="font-semibold text-slate-800">2019 - Dec 2024</span>
                          </div>
                          <div className="flex justify-between items-center py-1 border-b border-slate-50">
                            <span className="text-slate-450 font-medium font-semibold">Test Accuracy (R²)</span>
                            <span className="font-semibold text-slate-800">0.87</span>
                          </div>
                          <div className="flex justify-between items-center py-1 border-b border-slate-50">
                            <span className="text-slate-450 font-medium font-semibold">MAE</span>
                            <span className="font-semibold text-slate-800">0.06 GWh</span>
                          </div>
                          <div className="flex justify-between items-center py-1 border-b border-slate-50">
                            <span className="text-slate-450 font-medium font-semibold">RMSE</span>
                            <span className="font-semibold text-slate-800">0.08 GWh</span>
                          </div>
                        </div>
                        <div className="flex items-center gap-1.5 text-[9px] text-slate-400 font-semibold border-t border-slate-50 pt-2.5">
                          <Clock className="w-3.5 h-3.5" />
                          <span>Predictions are auto-updated weekly.</span>
                        </div>
                      </div>
                    </div>
                  </div>
                );
              })()}

              {dbTab === 'analytics' && (() => {
                const recommendedDistricts = [
                  { rank: 1, name: "Hyderabad", priority: "critical", demand: "0.35 GWh", gap: "0.18 GWh", growth: "21.3%", investment: "128 Cr", roi: "24.6%" },
                  { rank: 2, name: "Rangareddy", priority: "critical", demand: "0.22 GWh", gap: "0.12 GWh", growth: "19.8%", investment: "96 Cr", roi: "22.1%" },
                  { rank: 3, name: "Medchal-Malkajgiri", priority: "high", demand: "0.16 GWh", gap: "0.08 GWh", growth: "21.9%", investment: "88 Cr", roi: "21.3%" },
                  { rank: 4, name: "Sangareddy", priority: "high", demand: "0.12 GWh", gap: "0.07 GWh", growth: "18.7%", investment: "72 Cr", roi: "19.8%" },
                  { rank: 5, name: "Warangal Urban", priority: "medium", demand: "0.09 GWh", gap: "0.05 GWh", growth: "16.4%", investment: "54 Cr", roi: "17.2%" },
                  { rank: 6, name: "Nalgonda", priority: "medium", demand: "0.07 GWh", gap: "0.04 GWh", growth: "15.1%", investment: "46 Cr", roi: "16.4%" },
                  { rank: 7, name: "Karimnagar", priority: "medium", demand: "0.06 GWh", gap: "0.03 GWh", growth: "14.5%", investment: "38 Cr", roi: "15.1%" },
                  { rank: 8, name: "Nizamabad", priority: "medium", demand: "0.05 GWh", gap: "0.03 GWh", growth: "13.2%", investment: "34 Cr", roi: "14.8%" },
                ];
                
                const topDistrictsBarData = districtsList
                  .sort((a, b) => b.demand2026 - a.demand2026)
                  .slice(0, 10)
                  .map(d => {
                    const demand = parseFloat((d.demand2026 * 0.0338).toFixed(2));
                    const gap = parseFloat((demand * (0.35 + (d.priorityScore * 0.015))).toFixed(2));
                    return {
                      name: d.name.replace(" District", "").replace(" Urban", ""),
                      demand,
                      gap
                    };
                  });

                const distributionData = [
                  { name: "Hyderabad & RR", value: 28, fill: "#047857" },
                  { name: "Medchal-Malkajgiri", value: 16, fill: "#10b981" },
                  { name: "Sangareddy", value: 12, fill: "#34d399" },
                  { name: "Warangal", value: 8, fill: "#f59e0b" },
                  { name: "Nalgonda", value: 7, fill: "#8b5cf6" },
                  { name: "Others", value: 29, fill: "#cbd5e1" }
                ];

                const demandDrivers = [
                  { name: "Population Growth", value: 32 },
                  { name: "EV Adoption Rate", value: 27 },
                  { name: "Urbanization Level", value: 19 },
                  { name: "Income Level", value: 13 },
                  { name: "Road Network Density", value: 9 },
                ];

                return (
                  <div className="space-y-6">
                    {/* Header */}
                    <div className="flex flex-col xl:flex-row xl:items-center justify-between pb-4 border-b border-slate-100 gap-4">
                      <div>
                        <h2 className="text-xl font-bold text-slate-900 leading-tight">Analytics</h2>
                        <p className="text-xs text-slate-400 mt-1 font-medium">In-depth insights and data analytics for EV infrastructure planning</p>
                      </div>
                      <div className="flex flex-wrap items-center gap-3">
                        <div className="flex items-center gap-2 px-3 py-2 bg-white border border-slate-200 rounded-xl shadow-sm text-xs font-semibold text-slate-700">
                          <Calendar className="w-3.5 h-3.5 text-slate-400" />
                          <span>Jan 2024 - Dec 2026</span>
                          <ChevronDown className="w-3.5 h-3.5 text-slate-400 ml-1" />
                        </div>
                        <div className="flex items-center gap-2 px-3 py-2 bg-white border border-slate-200 rounded-xl shadow-sm text-xs font-semibold text-slate-700 cursor-pointer">
                          <Search className="w-3.5 h-3.5 text-slate-400" />
                          <span>Filters</span>
                        </div>
                        <button className="flex items-center gap-2 px-3 py-2 bg-emerald-50 text-emerald-800 rounded-xl hover:bg-emerald-100 transition-colors text-xs font-semibold shadow-sm cursor-pointer border-0">
                          <Download className="w-3.5 h-3.5" />
                          <span>Export Report</span>
                        </button>
                      </div>
                    </div>

                    {/* KPI Cards Row */}
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
                      {/* Card 1: Total EV Demand */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[120px]">
                        <div className="flex items-start justify-between">
                          <div className="p-2 rounded-xl bg-emerald-50 text-emerald-700">
                            <Zap className="w-4 h-4" />
                          </div>
                          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider text-right">Total EV Demand (2026)</span>
                        </div>
                        <div className="flex justify-between items-end mt-4">
                          <div>
                            <p className="text-xl font-extrabold text-slate-900 tracking-tight">1.24 GWh</p>
                            <p className="text-[10px] text-emerald-700 font-bold mt-1">+18.6% vs 2025 ↑</p>
                          </div>
                          <svg className="w-16 h-8 text-emerald-600 flex-shrink-0" viewBox="0 0 50 20">
                            <path d="M0 16 Q 10 12, 20 14 T 35 6 T 50 2" fill="none" stroke="currentColor" strokeWidth="2.0" strokeLinecap="round" />
                          </svg>
                        </div>
                      </div>

                      {/* Card 2: Total Charging Stations */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[120px]">
                        <div className="flex items-start justify-between">
                          <div className="p-2 rounded-xl bg-emerald-50 text-emerald-700">
                            <Layers className="w-4 h-4" />
                          </div>
                          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider text-right">Total Charging Stations</span>
                        </div>
                        <div className="flex justify-between items-end mt-4">
                          <div>
                            <p className="text-xl font-extrabold text-slate-900 tracking-tight">412</p>
                            <p className="text-[10px] text-emerald-700 font-bold mt-1">+24 this year ↑</p>
                          </div>
                          <svg className="w-16 h-8 text-emerald-600 flex-shrink-0" viewBox="0 0 50 20">
                            <path d="M0 18 Q 8 14, 16 16 T 28 8 T 40 10 T 50 2" fill="none" stroke="currentColor" strokeWidth="2.0" strokeLinecap="round" />
                          </svg>
                        </div>
                      </div>

                      {/* Card 3: Average Utilization Rate */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[120px]">
                        <div className="flex items-start justify-between">
                          <div className="p-2 rounded-xl bg-emerald-50 text-emerald-700">
                            <Activity className="w-4 h-4" />
                          </div>
                          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider text-right">Avg Utilization Rate</span>
                        </div>
                        <div className="flex justify-between items-end mt-4">
                          <div>
                            <p className="text-xl font-extrabold text-slate-900 tracking-tight">68%</p>
                            <p className="text-[10px] text-emerald-700 font-bold mt-1">+6.3% vs last year ↑</p>
                          </div>
                          <svg className="w-16 h-8 text-emerald-600 flex-shrink-0" viewBox="0 0 50 20">
                            <path d="M0 15 Q 12 12, 24 13 T 38 6 T 50 4" fill="none" stroke="currentColor" strokeWidth="2.0" strokeLinecap="round" />
                          </svg>
                        </div>
                      </div>

                      {/* Card 4: Capacity Gap (2026) */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[120px]">
                        <div className="flex items-start justify-between">
                          <div className="p-2 rounded-xl bg-orange-50 text-orange-655">
                            <Target className="w-4 h-4" />
                          </div>
                          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider text-right">Capacity Gap (2026)</span>
                        </div>
                        <div className="flex justify-between items-end mt-4">
                          <div>
                            <p className="text-xl font-extrabold text-slate-900 tracking-tight">0.56 GWh</p>
                            <p className="text-[10px] text-orange-655 font-bold mt-1">-8.2% vs 2025 ↓</p>
                          </div>
                          <svg className="w-16 h-8 text-orange-500 flex-shrink-0" viewBox="0 0 50 20">
                            <path d="M0 6 Q 10 12, 20 8 T 35 15 T 50 18" fill="none" stroke="currentColor" strokeWidth="2.0" strokeLinecap="round" />
                          </svg>
                        </div>
                      </div>

                      {/* Card 5: High Priority Districts */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between min-h-[120px]">
                        <div className="flex items-start justify-between">
                          <div className="p-2 rounded-xl bg-red-50 text-red-650">
                            <AlertTriangle className="w-4 h-4" />
                          </div>
                          <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider text-right">High Priority Districts</span>
                        </div>
                        <div className="mt-4">
                          <p className="text-xl font-extrabold text-slate-900 tracking-tight">
                            {districtsList.filter(d => d.priorityLevel === 'critical' || d.priorityLevel === 'high').length}
                          </p>
                          <p className="text-[10px] text-slate-400 font-semibold mt-1">Require immediate attention</p>
                        </div>
                      </div>
                    </div>

                    {/* Charts Row */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-4">
                      {/* Demand Distribution by District (span 4) */}
                      <div className="lg:col-span-4 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col justify-between min-h-[320px]">
                        <div>
                          <h4 className="text-sm font-semibold text-slate-900">Demand Distribution by District</h4>
                          <p className="text-xs text-slate-400 mt-0.5">Share of total predicted demand (2026)</p>
                        </div>
                        
                        <div className="flex flex-row items-center gap-4 my-4 flex-1">
                          <div className="relative w-36 h-36 flex items-center justify-center flex-shrink-0">
                            <div className="absolute flex flex-col items-center justify-center text-center">
                              <span className="text-base font-extrabold text-slate-900 leading-none">1.24</span>
                              <span className="text-[9px] font-bold text-slate-500 mt-0.5 leading-none">GWh</span>
                              <span className="text-[8px] text-slate-400 font-semibold leading-none mt-0.5">Total</span>
                            </div>
                            <ResponsiveContainer width="100%" height="100%">
                              <PieChart>
                                <Pie
                                  data={distributionData}
                                  cx="50%"
                                  cy="50%"
                                  innerRadius={45}
                                  outerRadius={62}
                                  paddingAngle={2}
                                  dataKey="value"
                                >
                                  {distributionData.map((cell, idx) => (
                                    <Cell key={idx} fill={cell.fill} />
                                  ))}
                                </Pie>
                              </PieChart>
                            </ResponsiveContainer>
                          </div>
                          
                          <div className="flex-1 flex flex-col gap-1.5 text-[11px]">
                            {distributionData.map((d, idx) => (
                              <div key={idx} className="flex items-center justify-between">
                                <div className="flex items-center gap-1 min-w-0">
                                  <span className="w-2 h-2 rounded-full flex-shrink-0" style={{ backgroundColor: d.fill }} />
                                  <span className="text-slate-500 font-semibold truncate">{d.name}</span>
                                </div>
                                <span className="font-bold text-slate-800 ml-1">{d.value}%</span>
                              </div>
                            ))}
                          </div>
                        </div>
                      </div>

                      {/* Demand vs Capacity Gap by District (span 5) */}
                      <div className="lg:col-span-5 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col min-h-[320px]">
                        <div>
                          <h4 className="text-sm font-semibold text-slate-900">Demand vs Capacity Gap (Top 10)</h4>
                          <p className="text-xs text-slate-400 mt-0.5">Predicted demand vs capacity gap by district (GWh)</p>
                        </div>
                        <div className="flex-1 min-h-[220px] mt-4">
                          <ResponsiveContainer width="100%" height="100%">
                            <BarChart data={topDistrictsBarData} margin={{ top: 10, right: 10, left: -22, bottom: 0 }}>
                              <CartesianGrid strokeDasharray="3 3" stroke="#f8fafc" vertical={false} />
                              <XAxis dataKey="name" stroke="#94A3B8" fontSize={9} tickLine={false} axisLine={false} />
                              <YAxis stroke="#94A3B8" fontSize={9} tickLine={false} axisLine={false} />
                              <Tooltip contentStyle={{ fontSize: '11px', borderRadius: '12px' }} />
                              <Legend verticalAlign="top" height={28} iconType="circle" wrapperStyle={{ fontSize: '10px' }} />
                              <Bar dataKey="demand" fill="#15803d" radius={[3, 3, 0, 0]} name="Predicted Demand" />
                              <Bar dataKey="gap" fill="#f97316" radius={[3, 3, 0, 0]} name="Capacity Gap" />
                            </BarChart>
                          </ResponsiveContainer>
                        </div>
                      </div>

                      {/* EV Demand Intensity Map (span 3) */}
                      <div className="lg:col-span-3 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col justify-between min-h-[320px]">
                        <div>
                          <h4 className="text-sm font-semibold text-slate-900">EV Demand Intensity Map (2026)</h4>
                          <p className="text-xs text-slate-400 mt-0.5">Predicted demand per sq. km</p>
                        </div>
                        <div className="flex-1 bg-slate-50 rounded-xl overflow-hidden relative min-h-[200px] mt-4">
                          <MapContainer 
                            center={[17.9784, 79.5941]} 
                            zoom={6.7} 
                            style={{ height: '100%', width: '100%' }}
                            zoomControl={false}
                            attributionControl={false}
                          >
                            <TileLayer
                              url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
                            />
                            {districtsList.map((d) => {
                              const intensityColor = d.demand2026 > 30 ? "#15803d" : d.demand2026 > 15 ? "#4ade80" : "#bbf7d0";
                              const radius = d.demand2026 > 30 ? 15 : d.demand2026 > 15 ? 11 : 7;
                              return (
                                <CircleMarker
                                  key={d.name}
                                  center={d.coordinates}
                                  radius={radius}
                                  fillColor={intensityColor}
                                  color="#ffffff"
                                  weight={1.5}
                                  opacity={0.9}
                                  fillOpacity={0.7}
                                />
                              );
                            })}
                          </MapContainer>
                          
                          {/* Legend overlay */}
                          <div className="absolute bottom-2.5 left-2.5 bg-white/95 backdrop-blur-sm border border-slate-100 rounded-lg p-1.5 text-[9px] font-semibold text-slate-650 shadow-sm z-[999] flex flex-col gap-1">
                            <div className="flex items-center gap-1">
                              <span className="w-2 h-2 bg-[#15803d] rounded-sm" />
                              <span>High</span>
                            </div>
                            <div className="flex items-center gap-1">
                              <span className="w-2 h-2 bg-[#4ade80] rounded-sm" />
                              <span>Medium</span>
                            </div>
                            <div className="flex items-center gap-1">
                              <span className="w-2 h-2 bg-[#bbf7d0] rounded-sm" />
                              <span>Low</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Recommended Districts and Right Stack Row */}
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-4">
                      {/* Left: Recommended Districts (span 7) */}
                      <div className="lg:col-span-7 bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col justify-between min-h-[480px]">
                        <div>
                          <h4 className="text-sm font-semibold text-slate-900">Recommended Districts for Investments</h4>
                          <p className="text-xs text-slate-400 mt-0.5">AI-ranked priority districts based on demand, capacity gap &amp; growth potential</p>
                        </div>
                        
                        <div className="overflow-x-auto my-4">
                          <table className="w-full text-left text-xs border-collapse">
                            <thead>
                              <tr className="text-slate-400 font-bold border-b border-slate-100">
                                <th className="py-2 px-1 text-center">Rank</th>
                                <th className="py-2 px-2">District</th>
                                <th className="py-2 px-2 text-center">Priority</th>
                                <th className="py-2 px-2 text-right">Demand (2026)</th>
                                <th className="py-2 px-2 text-right">Capacity Gap</th>
                                <th className="py-2 px-2 text-center">Growth (YoY)</th>
                                <th className="py-2 px-2 text-right">Investment</th>
                                <th className="py-2 px-2 text-right">ROI (5 Yr)</th>
                              </tr>
                            </thead>
                            <tbody>
                              {recommendedDistricts.map((item, idx) => (
                                <tr key={idx} className="border-b border-slate-50 last:border-0 hover:bg-slate-50/50 transition-colors">
                                  <td className="py-2 px-1 text-center font-bold text-slate-400">{item.rank}</td>
                                  <td className="py-2 px-2 font-semibold text-slate-800">{item.name}</td>
                                  <td className="py-2 px-2 text-center">
                                    <span className={`inline-block px-2 py-0.5 rounded text-[9px] font-bold uppercase tracking-wider ${
                                      item.priority === 'critical' ? 'bg-red-50 text-red-650' :
                                      item.priority === 'high' ? 'bg-orange-50 text-orange-600' :
                                      'bg-amber-50 text-amber-700'
                                    }`}>
                                      {item.priority}
                                    </span>
                                  </td>
                                  <td className="py-2 px-2 text-right font-semibold text-slate-800">{item.demand}</td>
                                  <td className="py-2 px-2 text-right text-slate-550 font-semibold">{item.gap}</td>
                                  <td className="py-2 px-2 text-center text-emerald-700 font-bold flex items-center justify-center gap-0.5">
                                    <TrendingUp className="w-3 h-3" />
                                    <span>{item.growth}</span>
                                  </td>
                                  <td className="py-2 px-2 text-right text-slate-850 font-semibold">{item.investment}</td>
                                  <td className="py-2 px-2 text-right text-emerald-800 font-bold">{item.roi}</td>
                                </tr>
                              ))}
                            </tbody>
                          </table>
                        </div>

                        <button 
                          onClick={() => setDbTab('explorer')}
                          className="w-full py-2.5 px-4 bg-emerald-50 text-emerald-800 border-0 hover:bg-emerald-100 transition-colors rounded-xl text-xs font-semibold flex items-center justify-center gap-1 shadow-sm cursor-pointer"
                        >
                          <span>View Full District Analysis</span>
                          <ArrowRight className="w-3.5 h-3.5" />
                        </button>
                      </div>

                      {/* Right: Stack of 3 Cards (span 5) */}
                      <div className="lg:col-span-5 flex flex-col gap-4">
                        {/* Card 1: Seasonal Demand Pattern */}
                        <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between flex-1">
                          <div className="mb-3">
                            <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Seasonal Demand Pattern (Statewide)</h4>
                            <p className="text-[10px] text-slate-400 font-semibold mt-0.5">Average demand (GWh)</p>
                          </div>
                          
                          <div className="overflow-x-auto">
                            <table className="w-full text-center text-[10px] font-semibold border-collapse">
                              <thead>
                                <tr className="text-slate-400 font-bold border-b border-slate-100">
                                  <th className="py-1 px-0.5 text-left">Year</th>
                                  {["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].map(m => (
                                    <th key={m} className="py-1 px-0.5 text-[9px]">{m}</th>
                                  ))}
                                </tr>
                              </thead>
                              <tbody>
                                {[
                                  { year: "2024", vals: [0.62, 0.65, 0.71, 0.75, 0.92, 1.02, 0.98, 0.90, 0.80, 0.68, 0.60, 0.58] },
                                  { year: "2025", vals: [0.68, 0.70, 0.77, 0.81, 0.88, 1.12, 1.08, 0.99, 0.89, 0.72, 0.64, 0.60] },
                                  { year: "2026 (F)", vals: [0.74, 0.76, 0.84, 0.88, 0.96, 1.24, 1.18, 1.07, 0.95, 0.78, 0.68, 0.65] }
                                ].map((row, idx) => (
                                  <tr key={idx} className="border-b border-slate-50 last:border-0">
                                    <td className="py-1 text-left font-bold text-slate-400 whitespace-nowrap text-[9px]">{row.year}</td>
                                    {row.vals.map((v, i) => {
                                      const bgStyle = v >= 1.1 ? "bg-emerald-700 text-white" : 
                                                      v >= 0.9 ? "bg-emerald-500 text-white" : 
                                                      v >= 0.75 ? "bg-emerald-200 text-emerald-900" : 
                                                      "bg-emerald-50 text-emerald-800";
                                      return (
                                        <td key={i} className={`py-1 px-0.5 text-[8px] rounded-sm font-bold ${bgStyle} transition-all hover:scale-105`}>
                                          {v.toFixed(2)}
                                        </td>
                                      );
                                    })}
                                  </tr>
                                ))}
                              </tbody>
                            </table>
                          </div>
                        </div>

                        {/* Card 2: Demand Drivers Impact */}
                        <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between flex-1">
                          <div className="mb-3">
                            <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Demand Drivers Impact (Top 5)</h4>
                            <p className="text-[10px] text-slate-400 font-semibold mt-0.5">Impact on EV demand (2026)</p>
                          </div>
                          
                          <div className="space-y-2">
                            {demandDrivers.map((driver, idx) => (
                              <div key={idx} className="flex items-center gap-3">
                                <span className="w-24 text-[10px] font-semibold text-slate-600 truncate leading-none">{driver.name}</span>
                                <div className="flex-1 h-1.5 bg-slate-50 border border-slate-100 rounded-full overflow-hidden">
                                  <div className="h-full bg-emerald-700 rounded-full" style={{ width: `${driver.value * 2.5}%` }} />
                                </div>
                                <span className="w-8 text-right text-[10px] font-bold text-slate-700 leading-none">0.{driver.value}</span>
                              </div>
                            ))}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                );
              })()}

              {dbTab === 'assistant' && (
                <div className="space-y-6 flex flex-col h-[calc(100vh-110px)]">
                  {/* Header */}
                  <div className="flex flex-col xl:flex-row xl:items-center justify-between pb-4 border-b border-slate-100 gap-4 flex-shrink-0">
                    <div>
                      <h2 className="text-xl font-bold text-slate-900 leading-tight">AI Assistant</h2>
                      <p className="text-xs text-slate-400 mt-1 font-medium">Your intelligent partner for EV infrastructure insights</p>
                    </div>
                    <div className="flex flex-wrap items-center gap-3">
                      <div className="flex items-center gap-2 px-3 py-2 bg-white border border-slate-200 rounded-xl shadow-sm text-xs font-semibold text-slate-700">
                        <Calendar className="w-3.5 h-3.5 text-slate-400" />
                        <span>Jan 2024 - Dec 2026</span>
                        <ChevronDown className="w-3.5 h-3.5 text-slate-400 ml-1" />
                      </div>
                    </div>
                  </div>

                  {/* Body Grid */}
                  <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 flex-1 min-h-0">
                    {/* Left Column: Chat Area (span 8) */}
                    <div className="lg:col-span-8 bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between h-full min-h-0">
                      {/* Messages Container */}
                      <div className="flex-1 overflow-y-auto pr-1 space-y-4 mb-3">
                        {chatHistory.map((msg, index) => {
                          if (msg.isGreeting) {
                            return (
                              <div key={index} className="flex gap-4 p-5 bg-slate-50/40 border border-slate-100 rounded-2xl mb-4 items-center">
                                <div className="w-12 h-12 rounded-full bg-emerald-50 text-emerald-700 flex items-center justify-center flex-shrink-0 shadow-sm border border-emerald-100/50">
                                  <Bot className="w-6 h-6" />
                                </div>
                                <div className="min-w-0">
                                  <h4 className="text-sm font-bold text-slate-800">Hello! I'm <span className="text-emerald-700 font-extrabold">EVision</span> AI Assistant</h4>
                                  <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">
                                    Ask me anything about EV infrastructure in Telangana. I can help you analyze data, generate insights, and support better decision-making.
                                  </p>
                                </div>
                              </div>
                            );
                          }

                          const isUser = msg.sender === 'user';
                          return (
                            <div key={index} className={`flex ${isUser ? 'justify-end' : 'justify-start'} gap-3 items-start`}>
                              {!isUser && (
                                <div className="w-8 h-8 rounded-full bg-emerald-50 text-emerald-700 flex items-center justify-center flex-shrink-0 border border-emerald-100 shadow-sm">
                                  <Bot className="w-4 h-4" />
                                </div>
                              )}
                              <div className="max-w-[85%] flex flex-col">
                                <div className={`rounded-2xl px-4 py-3 text-xs leading-relaxed border ${
                                  isUser 
                                    ? 'bg-slate-50/80 border-slate-200/50 text-slate-800 rounded-tr-none shadow-sm' 
                                    : 'bg-white border-slate-150 text-slate-800 shadow-sm rounded-tl-none'
                                }`}>
                                  <p className="font-medium whitespace-pre-wrap">{msg.text}</p>
                                  
                                  {/* Render Table in Chat if required */}
                                  {!isUser && msg.showTable && (
                                    <div className="overflow-x-auto my-3 border border-slate-100 rounded-xl p-2 bg-slate-50/50">
                                      <table className="w-full text-left text-[10px] border-collapse">
                                        <thead>
                                          <tr className="text-slate-400 font-bold border-b border-slate-100">
                                            <th className="py-1.5 px-1 text-center">Rank</th>
                                            <th className="py-1.5 px-2">District</th>
                                            <th className="py-1.5 px-2 text-center">Priority</th>
                                            <th className="py-1.5 px-2 text-right">Demand (2026)</th>
                                            <th className="py-1.5 px-2 text-right">Capacity Gap</th>
                                            <th className="py-1.5 px-2 text-center">Growth Potential</th>
                                          </tr>
                                        </thead>
                                        <tbody>
                                          {[
                                            { rank: 1, name: "Hyderabad", priority: "critical", demand: "0.35 GWh", gap: "0.18 GWh", growth: "High" },
                                            { rank: 2, name: "Rangareddy", priority: "critical", demand: "0.22 GWh", gap: "0.12 GWh", growth: "High" },
                                            { rank: 3, name: "Medchal-Malkajgiri", priority: "high", demand: "0.16 GWh", gap: "0.08 GWh", growth: "High" },
                                            { rank: 4, name: "Sangareddy", priority: "high", demand: "0.12 GWh", gap: "0.07 GWh", growth: "High" },
                                            { rank: 5, name: "Warangal Urban", priority: "medium", demand: "0.09 GWh", gap: "0.05 GWh", growth: "Medium" }
                                          ].map((row, idx) => (
                                            <tr key={idx} className="border-b border-slate-100/55 last:border-0">
                                              <td className="py-1 text-center font-bold text-slate-400">{row.rank}</td>
                                              <td className="py-1 font-semibold text-slate-800">{row.name}</td>
                                              <td className="py-1 text-center">
                                                <span className={`inline-block px-1.5 py-0.5 rounded text-[8px] font-bold uppercase tracking-wide ${
                                                  row.priority === 'critical' ? 'bg-red-50 text-red-650' :
                                                  row.priority === 'high' ? 'bg-orange-50 text-orange-600' :
                                                  'bg-amber-50 text-amber-700'
                                                }`}>
                                                  {row.priority}
                                                </span>
                                              </td>
                                              <td className="py-1 text-right font-semibold text-slate-800">{row.demand}</td>
                                              <td className="py-1 text-right text-slate-500">{row.gap}</td>
                                              <td className="py-1 text-center font-bold text-emerald-800">{row.growth}</td>
                                            </tr>
                                          ))}
                                        </tbody>
                                      </table>
                                    </div>
                                  )}
                                  
                                  {/* Subtext under table if any */}
                                  {!isUser && msg.subtext && (
                                    <p className="text-[11px] text-slate-500 mt-2 font-medium leading-relaxed">{msg.subtext}</p>
                                  )}
                                </div>
                                {msg.timestamp && (
                                  <span className={`text-[9px] text-slate-400 font-semibold mt-1 flex items-center gap-0.5 ${isUser ? 'self-end' : 'self-start'}`}>
                                    {isUser && <Check className="w-2.5 h-2.5 text-emerald-600" />}
                                    <span>{msg.timestamp}</span>
                                  </span>
                                )}
                              </div>
                            </div>
                          );
                        })}
                        <div ref={chatEndRef} />
                      </div>

                      {/* Chat Footer Wrapper */}
                      <div className="flex-shrink-0 pt-2 border-t border-slate-100">
                        {/* Suggestion Chips */}
                        <div className="flex flex-wrap gap-2 mb-3">
                          {[
                            { text: "Show Hyderabad insights", query: "Show Hyderabad insights", icon: MapPin },
                            { text: "Compare top 3 districts", query: "Compare the top 3 priority districts", icon: BarChart2 },
                            { text: "Why is Rangareddy critical?", query: "Why is Rangareddy ranked as critical priority?", icon: AlertTriangle }
                          ].map((chip, i) => {
                            const Icon = chip.icon;
                            return (
                              <button
                                key={i}
                                onClick={() => handleSendChat(chip.query)}
                                className="flex items-center gap-1 px-2.5 py-1 bg-emerald-50/50 text-emerald-800 border border-emerald-100/40 hover:bg-emerald-100 hover:border-emerald-200 transition-all rounded-xl text-[10px] font-semibold cursor-pointer shadow-sm"
                              >
                                <Icon className="w-3 h-3 text-emerald-700" />
                                <span>{chip.text}</span>
                              </button>
                            );
                          })}
                        </div>

                        {/* Input Area */}
                        <div className="flex items-center gap-2 relative bg-slate-50 border border-slate-200 rounded-xl px-4 py-1.5 focus-within:ring-2 focus-within:ring-emerald-100 focus-within:border-emerald-750 transition-all">
                          <input
                            type="text"
                            value={chatInput}
                            onChange={(e) => setChatInput(e.target.value)}
                            onKeyDown={(e) => e.key === 'Enter' && handleSendChat()}
                            placeholder="Ask a question about EV infrastructure, demand, districts..."
                            className="flex-grow bg-transparent border-0 outline-none text-xs text-slate-700 placeholder:text-slate-400 py-1.5"
                          />
                          <button 
                            onClick={() => handleSendChat()}
                            className="w-8 h-8 rounded-full bg-emerald-700 hover:bg-emerald-800 text-white flex items-center justify-center transition-colors shadow-sm cursor-pointer"
                          >
                            <Send className="w-3.5 h-3.5" />
                          </button>
                        </div>
                        
                        {/* Info Caption */}
                        <p className="text-[9px] text-slate-400 font-semibold mt-2 flex items-center gap-1">
                          <ShieldCheck className="w-3.5 h-3.5 text-slate-400" />
                          <span>AI responses are generated based on data and models. Please verify critical decisions.</span>
                        </p>
                      </div>
                    </div>

                    {/* Right Column: Sidebar (span 4) */}
                    <div className="lg:col-span-4 flex flex-col gap-4 h-full min-h-0 overflow-y-auto">
                      {/* Suggested Questions */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between">
                        <div className="mb-3 flex items-center gap-2">
                          <div className="p-1 rounded bg-emerald-50 text-emerald-700">
                            <MessageSquare className="w-3.5 h-3.5" />
                          </div>
                          <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Suggested Questions</h4>
                        </div>
                        
                        <div className="space-y-2.5">
                          {[
                            { text: "Which districts have the highest demand?", icon: TrendingUp },
                            { text: "Show districts with highest capacity gap", icon: Target },
                            { text: "What is the demand forecast for Hyderabad?", icon: BarChart2 },
                            { text: "Compare Warangal and Nizamabad", icon: Activity },
                            { text: "Which areas have low coverage?", icon: Layers },
                          ].map((q, idx) => {
                            const Icon = q.icon;
                            return (
                              <button
                                key={idx}
                                onClick={() => handleSendChat(q.text)}
                                className="w-full flex items-center justify-between p-2.5 bg-slate-50 border border-slate-100 hover:border-emerald-200 hover:bg-emerald-50/30 text-left rounded-xl transition-all group cursor-pointer"
                              >
                                <div className="flex items-center gap-2 min-w-0">
                                  <Icon className="w-3.5 h-3.5 text-emerald-700 flex-shrink-0" />
                                  <span className="text-[11px] font-semibold text-slate-655 truncate group-hover:text-emerald-950">{q.text}</span>
                                </div>
                                <ArrowRight className="w-3 h-3 text-emerald-700 transition-transform group-hover:translate-x-0.5 flex-shrink-0 ml-2" />
                              </button>
                            );
                          })}
                        </div>
                        
                        <button className="w-full text-center text-[10px] font-bold text-emerald-750 hover:text-emerald-800 transition-colors pt-3 border-t border-slate-50 mt-3.5 bg-transparent border-0 cursor-pointer">
                          View all questions
                        </button>
                      </div>

                      {/* Quick Actions */}
                      <div className="bg-white rounded-2xl border border-slate-100 shadow-sm p-4 flex flex-col justify-between">
                        <div className="mb-3 flex items-center gap-2">
                          <div className="p-1 rounded bg-emerald-50 text-emerald-700">
                            <Zap className="w-3.5 h-3.5" />
                          </div>
                          <h4 className="text-xs font-bold text-slate-900 uppercase tracking-wider">Quick Actions</h4>
                        </div>
                        
                        <div className="grid grid-cols-2 gap-2 text-[10px]">
                          {[
                            { title: "Forecast Demand", desc: "Get future demand forecasts", query: "Show demand forecasts for all districts", icon: TrendingUp },
                            { title: "District Comparison", desc: "Compare districts side by side", query: "Compare the top districts by EV demand and capacity", icon: BarChart2 },
                            { title: "Investment Insights", desc: "Identify high ROI opportunities", query: "Which districts offer the highest investment ROI?", icon: Target },
                            { title: "Find Optimal Locations", desc: "Get AI-recommended locations", query: "What are the recommended deployment areas for charging stations?", icon: MapPin },
                          ].map((action, i) => {
                            const Icon = action.icon;
                            return (
                              <button
                                key={i}
                                onClick={() => handleSendChat(action.query)}
                                className="p-2.5 bg-emerald-50/20 border border-emerald-100/50 hover:bg-emerald-50/70 hover:border-emerald-200 transition-all rounded-xl text-left flex flex-col justify-between min-h-[75px] group cursor-pointer"
                              >
                                <div className="p-1 rounded bg-white text-emerald-700 w-fit shadow-xs">
                                  <Icon className="w-3.5 h-3.5" />
                                </div>
                                <div className="mt-2.5">
                                  <p className="font-bold text-slate-800 leading-tight group-hover:text-emerald-950">{action.title}</p>
                                  <p className="text-[8px] text-slate-400 mt-0.5 leading-none">{action.desc}</p>
                                </div>
                              </button>
                            );
                          })}
                        </div>
                      </div>

                    </div>
                  </div>
                </div>
              )}
            </main>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

export default App;
