const apiBase = import.meta.env.VITE_API_BASE_URL || 'https://jansetu-api-3sn63mklua-el.a.run.app';

const postAi = async (path, payload) => {
  const response = await fetch(`${apiBase}${path}`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
  });
  if (!response.ok) throw new Error('AI service is temporarily unavailable.');
  return response.json();
};

export const verifyReportWithAi = (payload) => postAi('/api/verify-report', payload);
export const getAreaInsights = (payload) => postAi('/api/area-insights', payload);
