import { useState } from 'react';
import LandingPage from './imports/LandingPage';
import SignInPage from './components/SignInPage';
import CreateAccountPage from './components/CreateAccountPage';
import ForgotPasswordPage from './components/ForgotPasswordPage';
import FormPage from './components/FormPage';
import ExplorePage from './components/ExplorePage';
import RecommendationPage from './components/RecommendationPage';
import ProfilePage from './components/ProfilePage';

type Page = 'landing' | 'signin' | 'create-account' | 'forgot-password' | 'form' | 'explore' | 'recommendations' | 'profile';

interface RSO {
  id: number;
  name: string;
  tags?: string;
}

export default function App() {
  const [currentPage, setCurrentPage] = useState<Page>('landing');
  const [savedRSOs, setSavedRSOs] = useState<RSO[]>([]);
  const [selectedRSOs, setSelectedRSOs] = useState<RSO[]>([]);

  const navigateTo = (page: Page) => {
    setCurrentPage(page);
  };

  const handleExploreSubmit = (selected: RSO[]) => {
    setSelectedRSOs(selected);
    navigateTo('recommendations');
  };

  const handleSaveToProfile = (starred: RSO[]) => {
    setSavedRSOs(starred);
    navigateTo('profile');
  };

  return (
    <div className="min-h-screen">
      {currentPage === 'landing' && (
        <LandingPage onGetStarted={() => navigateTo('signin')} />
      )}
      {currentPage === 'signin' && (
        <SignInPage
          onSignIn={() => navigateTo('profile')}
          onCreateAccount={() => navigateTo('create-account')}
          onForgotPassword={() => navigateTo('forgot-password')}
        />
      )}
      {currentPage === 'create-account' && (
        <CreateAccountPage onBack={() => navigateTo('signin')} />
      )}
      {currentPage === 'forgot-password' && (
        <ForgotPasswordPage onBack={() => navigateTo('signin')} />
      )}
      {currentPage === 'profile' && (
        <ProfilePage 
          savedRSOs={savedRSOs}
          onRecommendMeClubs={() => navigateTo('form')}
          onLogout={() => navigateTo('landing')}
        />
      )}
      {currentPage === 'form' && (
        <FormPage onSubmit={() => navigateTo('explore')} />
      )}
      {currentPage === 'explore' && (
        <ExplorePage onSubmit={handleExploreSubmit} />
      )}
      {currentPage === 'recommendations' && (
        <RecommendationPage 
          rsos={selectedRSOs}
          onSaveToProfile={handleSaveToProfile}
        />
      )}
    </div>
  );
}