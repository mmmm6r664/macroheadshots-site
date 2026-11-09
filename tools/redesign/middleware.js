// Vercel Routing Middleware: deny visitors from African countries and territories.
// Vercel sets x-vercel-ip-country (ISO 3166-1 alpha-2) on every request at the edge;
// clients cannot override it.
const BLOCKED = new Set([
  'DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CV', 'CM', 'CF', 'TD', 'KM', 'CG', 'CD', 'CI',
  'DJ', 'EG', 'GQ', 'ER', 'SZ', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR',
  'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'ST', 'SN',
  'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW',
  // territories on the African continent
  'EH', 'RE', 'YT', 'SH', 'IO', 'TF',
]);

export const config = { matcher: '/:path*' };

export default function middleware(request) {
  const country = (request.headers.get('x-vercel-ip-country') || '').toUpperCase();
  if (BLOCKED.has(country)) {
    return new Response('This website is not available in your region.', {
      status: 403,
      headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store' },
    });
  }
  // fall through: serve the static site as normal
}
