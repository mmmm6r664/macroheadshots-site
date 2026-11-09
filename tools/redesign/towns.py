"""Town-specific content for the local landing pages (unique copy per town for local SEO)."""

TOWN_INFO = {
    "totowa": dict(
        kind="borough", county="Passaic County",
        desc="Headshot studio right here in Totowa, NJ. Corporate, acting, residency (ERAS) and personal branding headshots, retouched within 24 hours. Book today.",
        lead="Our studio is right here in Totowa, on US-46 — the easiest headshot session you will ever book. Corporate, acting, residency and personal branding portraits, retouched within 24 hours.",
        intro=[
            "Macro Headshots is a Totowa business. Our studio sits at 195 US-46, Suite 9, so for anyone who lives or works in Totowa a polished new headshot is only a few minutes away — perfect for squeezing a session into a lunch break or between meetings.",
            "Totowa's location where US-46 and I-80 meet makes it a crossroads for North Jersey professionals. Business owners along the Route 46 corridor, commuters heading toward Manhattan and local students all come to us for clean, confident headshots for LinkedIn, company websites and applications.",
        ],
        route="We are on US-46 in Totowa, a short drive from anywhere in the borough. Parking is available on site at the building.",
        highlights=["US-46 business corridor", "I-80 access", "Borders Wayne, Paterson, Little Falls, Haledon & Woodland Park"],
        neighbors=["wayne", "woodland-park", "little-falls", "paterson", "haledon"],
        faqs=[
            ("Where exactly is your Totowa studio?", "We are at 195 US-46, Suite 9, Totowa, NJ 07512 — on the Route 46 corridor with easy access from I-80."),
            ("Can I book a quick headshot during my lunch break in Totowa?", "Yes. Our 1-headshot package is a 5-minute session, and every photo is retouched and delivered within 24 hours."),
        ]),
    "wayne": dict(
        kind="township", county="Passaic County",
        desc="Professional headshots for Wayne, NJ professionals, WPU students and realtors. Studio minutes away in neighboring Totowa. Retouched in 24 hours.",
        lead="Professional headshots for Wayne — from corporate teams and realtors to William Paterson University students — at our studio in neighboring Totowa.",
        intro=[
            "Wayne is one of Passaic County's largest communities, with a busy business district along Routes 23, 46 and I-80, Willowbrook Mall, and William Paterson University. That mix of corporate offices, retail, real estate and higher education means plenty of people who need a sharp, current headshot.",
            "Because Wayne borders Totowa, our studio is a quick drive away. We photograph Wayne professionals updating LinkedIn and company bios, realtors who need a fresh agent photo, and WPU students and graduates preparing résumés, graduate school and residency applications.",
        ],
        route="Wayne borders Totowa. Take US-46 East or I-80 East toward Totowa — our studio is on US-46.",
        highlights=["William Paterson University", "Willowbrook Mall", "Dey Mansion (Washington's Headquarters)", "Routes 23, 46 & I-80"],
        neighbors=["totowa", "little-falls", "pompton-lakes", "haledon", "north-haledon"],
        faqs=[
            ("Do you photograph William Paterson University students?", "Yes. Students and graduates come to us for résumé, LinkedIn, graduate school and residency (ERAS) headshots. Sessions start at $50."),
            ("How far is your studio from Wayne?", "Wayne borders Totowa, so our studio on US-46 is a short drive via US-46 or I-80."),
        ]),
    "paterson": dict(
        kind="city", county="Passaic County",
        desc="Headshots for Paterson, NJ professionals, healthcare teams and residency applicants. Studio next door in Totowa. Retouched and delivered in 24 hours.",
        lead="Headshots for Paterson's professionals, healthcare teams and residency applicants — at our studio just across the border in Totowa.",
        intro=[
            "Paterson — the Silk City and Passaic County's seat — is one of New Jersey's largest cities, home to the Great Falls, St. Joseph's University Medical Center and Passaic County Community College. It is a city of hospital staff, county and city employees, small-business owners, attorneys and students.",
            "Paterson borders Totowa, so our studio is close by. We regularly create headshots for healthcare professionals and medical residency applicants who need an ERAS-ready photo, for professionals who need an updated LinkedIn or staff photo, and for local business owners building their brand.",
        ],
        route="Paterson borders Totowa. Head west on US-46 or Union Boulevard into Totowa — our studio is on US-46.",
        highlights=["Paterson Great Falls National Historical Park", "St. Joseph's University Medical Center", "Passaic County Community College", "Passaic County seat"],
        neighbors=["totowa", "woodland-park", "haledon", "prospect-park", "clifton"],
        faqs=[
            ("Do you offer ERAS headshots for residency applicants in Paterson?", "Yes. We deliver a version sized for the ERAS upload (2.5 × 3.5 in, 375 × 525 px, JPG under 150 KB) along with your full-resolution, retouched photos."),
            ("Can you photograph a team from a Paterson office or hospital department?", "Yes. Call us at 877-622-4973 to plan a group of sessions so your whole team has consistent headshots."),
        ]),
    "clifton": dict(
        kind="city", county="Passaic County",
        desc="Headshots for Clifton, NJ: corporate, acting, personal branding and residency photos. Studio in nearby Totowa via Route 46. Retouched within 24 hours.",
        lead="Corporate, acting and personal branding headshots for Clifton — a quick trip west on Route 46 to our Totowa studio.",
        intro=[
            "Clifton is Passaic County's second-largest city, crossed by the Garden State Parkway, Route 3 and Route 46 and home to busy shopping centers like Clifton Commons. Its corporate offices, healthcare practices, retail businesses and many commuters make it a city full of professionals who are always being looked up online.",
            "Clifton sits next to Montclair State University and is an easy drive to our studio in Totowa along Route 46. We create crisp headshots for Clifton professionals and job seekers, personal branding portraits for consultants and realtors, and acting headshots for performers heading into the city for auditions.",
        ],
        route="From Clifton, take US-46 West toward Totowa. Our studio is on US-46, just past Little Falls and Woodland Park.",
        highlights=["Garden State Parkway, Route 3 & Route 46", "Clifton Commons", "Next to Montclair State University"],
        neighbors=["passaic", "little-falls", "woodland-park", "paterson"],
        faqs=[
            ("Is your studio easy to reach from Clifton?", "Yes — take US-46 West toward Totowa; our studio is right on Route 46."),
            ("Do you do acting headshots for Clifton performers?", "Yes. Our acting headshots are designed to show personality, with sessions from 5 to 60 minutes and natural-looking retouching."),
        ]),
    "passaic": dict(
        kind="city", county="Passaic County",
        desc="Professional headshots for Passaic, NJ: healthcare, business and residency (ERAS) photos. Studio in nearby Totowa. Retouched and delivered in 24 hours.",
        lead="Professional headshots for the city of Passaic — healthcare, business and residency photos at our nearby Totowa studio.",
        intro=[
            "The city of Passaic is a dense, diverse community on the Passaic River and home to St. Mary's General Hospital. Healthcare workers, small-business owners, educators and commuters all need professional photos for work badges, websites, LinkedIn and applications.",
            "We make it simple for Passaic residents to get a polished headshot. Our Totowa studio is a short drive away, sessions start at just 5 minutes, and every image is retouched and delivered within 24 hours — including ERAS-ready photos for medical residency applicants.",
        ],
        route="From Passaic, head west through Clifton to US-46 West toward Totowa — our studio is on US-46.",
        highlights=["St. Mary's General Hospital", "Passaic River", "Diverse, walkable downtown"],
        neighbors=["clifton", "paterson", "little-falls"],
        faqs=[
            ("Do you offer headshots for healthcare staff in Passaic?", "Yes. We photograph healthcare professionals for staff pages and badges, and residency applicants for ERAS."),
            ("How quickly will I get my photos?", "Every photo is retouched and delivered within 24 hours of your session."),
        ]),
    "little-falls": dict(
        kind="township", county="Passaic County",
        desc="Headshots for Little Falls, NJ — next door to our Totowa studio. Ideal for Montclair State students, professionals and creators. Retouched in 24 hours.",
        lead="Little Falls is right next door to our Totowa studio — the perfect spot for Montclair State students, professionals and creators to get a standout headshot.",
        intro=[
            "Little Falls borders Totowa, sits along the Passaic River and shares part of the Montclair State University campus — including the Yogi Berra Museum & Learning Center. Commuters ride NJ Transit from Little Falls station, and the township is full of young professionals, faculty and students.",
            "That makes Little Falls one of our closest neighbors. We photograph MSU students and graduates for LinkedIn, résumés and graduate or residency applications, professors and staff for faculty pages, and local creators and consultants who want branding photos that feel like them.",
        ],
        route="Little Falls borders Totowa. Take Route 46 West or Main Street into Totowa — our studio is on US-46.",
        highlights=["Montclair State University (part of campus)", "Yogi Berra Museum & Learning Center", "Little Falls NJ Transit station", "Passaic River"],
        neighbors=["totowa", "woodland-park", "wayne", "clifton"],
        faqs=[
            ("Do you do headshots for Montclair State University students?", "Yes. Students and graduates book us for LinkedIn, résumés, graduate school and residency (ERAS) photos. Packages start at $50."),
            ("How close is the studio to Little Falls?", "Very close — Little Falls borders Totowa, and our studio is on US-46."),
        ]),
    "woodland-park": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Woodland Park, NJ — just across the border from our Totowa studio. Corporate, acting and personal branding photos, retouched in 24 hours.",
        lead="Woodland Park borders Totowa, so a polished new headshot is just minutes from home — corporate, acting and personal branding sessions.",
        intro=[
            "Woodland Park — known as West Paterson until 2008 — sits at the foot of Garret Mountain Reservation, with US-46 and I-80 running through town. Its office parks, retail and easy highway access make it home to plenty of commuters and business professionals.",
            "Woodland Park shares a border with Totowa, so our studio is one of the closest you can find. Stop by for a quick corporate headshot, a fresh LinkedIn photo, or a longer personal branding session with multiple looks.",
        ],
        route="Woodland Park borders Totowa. Take US-46 West into Totowa — our studio is right on Route 46.",
        highlights=["Garret Mountain Reservation", "US-46 & I-80", "Formerly West Paterson"],
        neighbors=["totowa", "little-falls", "paterson", "clifton"],
        faqs=[
            ("Is your studio close to Woodland Park?", "Yes — Woodland Park borders Totowa, and we are on US-46."),
            ("Can I get several looks in one session?", "Yes. Longer sessions (30 or 60 minutes) give you time for outfit changes and different backgrounds."),
        ]),
    "haledon": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Haledon, NJ residents and nearby William Paterson University students. Studio in neighboring Totowa. Retouched and delivered in 24 hours.",
        lead="Headshots for Haledon residents and nearby William Paterson University students — at our studio in neighboring Totowa.",
        intro=[
            "Haledon is a close-knit borough with a proud history — it is home to the Botto House, the American Labor Museum, a National Historic Landmark. It sits beside William Paterson University, so the community includes many students, faculty and young professionals.",
            "Haledon borders Totowa, which makes our studio an easy stop. Students and graduates come to us for résumé, LinkedIn and residency application photos, and local professionals and business owners book quick sessions to refresh their online presence.",
        ],
        route="Haledon borders Totowa. Head south toward US-46 in Totowa — our studio is on Route 46.",
        highlights=["Botto House / American Labor Museum", "Next to William Paterson University", "Borders Totowa"],
        neighbors=["totowa", "north-haledon", "prospect-park", "paterson", "wayne"],
        faqs=[
            ("Do Haledon students get headshots for job applications?", "Yes — students and recent graduates book our 5- and 15-minute packages for résumés, LinkedIn and applications."),
            ("Are all photos retouched?", "Yes. Every photo is professionally retouched and delivered within 24 hours."),
        ]),
    "north-haledon": dict(
        kind="borough", county="Passaic County",
        desc="Professional headshots for North Haledon, NJ. Corporate, personal branding and residency photos at our nearby Totowa studio. Retouched in 24 hours.",
        lead="Polished corporate, personal branding and residency headshots for North Haledon — at our studio a short drive south in Totowa.",
        intro=[
            "North Haledon is a quiet, residential borough near High Mountain Park Preserve and William Paterson University. Many residents are commuting professionals, business owners and families with students heading to college or graduate programs.",
            "We help North Haledon professionals look their best online and on paper — from executive and LinkedIn headshots to personal branding portraits for consultants and realtors, and ERAS-ready photos for medical residency applicants.",
        ],
        route="From North Haledon, head south through Haledon toward US-46 in Totowa — our studio is on Route 46.",
        highlights=["High Mountain Park Preserve", "Near William Paterson University", "Residential community"],
        neighbors=["haledon", "prospect-park", "hawthorne", "wayne"],
        faqs=[
            ("What should I wear for a corporate headshot?", "Solid colors and well-fitted business attire photograph best. Bring an extra top or jacket if you want more than one look."),
            ("Do you offer residency headshots?", "Yes. We deliver an ERAS-sized version along with your full-resolution, retouched photos."),
        ]),
    "prospect-park": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Prospect Park, NJ — Passaic County's smallest borough. Professional photos at our nearby Totowa studio, retouched within 24 hours.",
        lead="Professional headshots for Prospect Park — Passaic County's smallest borough — just a few minutes from our Totowa studio.",
        intro=[
            "Prospect Park is Passaic County's smallest municipality, under half a square mile, bordered by Haledon, Hawthorne, North Haledon and Paterson. It is a dense, diverse, walkable community where neighbors run small businesses, work in healthcare and commute across North Jersey.",
            "We make professional photos easy for Prospect Park residents: book a quick 5-minute session for a work or LinkedIn photo, or a longer session for personal branding. Every photo is retouched and ready within 24 hours.",
        ],
        route="From Prospect Park, head southwest through Haledon or Paterson to US-46 in Totowa — our studio is on Route 46.",
        highlights=["Passaic County's smallest borough", "Named after Brooklyn's Prospect Park", "Borders Haledon, Hawthorne, North Haledon & Paterson"],
        neighbors=["haledon", "north-haledon", "hawthorne", "paterson"],
        faqs=[
            ("How much does a headshot cost?", "Packages start at $50 for one headshot from a 5-minute session, up to $250 for 10 headshots from a 1-hour session."),
            ("Can small-business owners get branding photos?", "Yes — our personal branding sessions are ideal for owners who want photos for their website, social media and marketing."),
        ]),
    "hawthorne": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Hawthorne, NJ commuters, professionals and creators. Studio in nearby Totowa. Corporate and personal branding photos, retouched in 24 hours.",
        lead="Headshots for Hawthorne's commuters, professionals and creators — corporate and personal branding portraits at our Totowa studio.",
        intro=[
            "Hawthorne is a close-knit borough known for Goffle Brook Park, a county park designed by the Olmsted Brothers. With Route 208 running through town and a station on NJ Transit's Main Line, it is home to many commuters who work in Bergen County, Passaic County and New York City.",
            "Hawthorne professionals book us for corporate and LinkedIn headshots, and local creators, realtors and consultants come in for personal branding sessions with multiple looks. Every photo is retouched and delivered within 24 hours.",
        ],
        route="From Hawthorne, head southwest through Paterson to US-46 West into Totowa — our studio is on Route 46.",
        highlights=["Goffle Brook Park (Olmsted Brothers design)", "NJ Transit Main Line station", "Route 208"],
        neighbors=["prospect-park", "north-haledon", "paterson", "haledon"],
        faqs=[
            ("Do you offer headshots for Hawthorne realtors?", "Yes. Our personal branding sessions give realtors friendly, professional photos for listings, signs and online profiles."),
            ("How long is a session?", "From 5 minutes for one headshot up to an hour for 10 headshots and multiple looks."),
        ]),
    "pompton-lakes": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Pompton Lakes, NJ professionals and creators. Studio a short drive south in Totowa. Corporate and branding photos, retouched in 24 hours.",
        lead="Corporate and personal branding headshots for Pompton Lakes — a short drive south to our Totowa studio.",
        intro=[
            "Pompton Lakes sits where the Ramapo, Pequannock and Wanaque rivers meet, about 20 miles northwest of Midtown Manhattan, with Ramapo Mountain State Forest just beyond town. Its residents include commuters, small-business owners and professionals across North Jersey.",
            "We help Pompton Lakes professionals put their best face forward — with crisp corporate headshots for LinkedIn and company sites, and relaxed personal branding portraits for consultants, coaches, realtors and creators.",
        ],
        route="From Pompton Lakes, take Route 23 South or I-287 South toward Wayne and US-46 East into Totowa — our studio is on Route 46.",
        highlights=["Ramapo, Pequannock & Wanaque rivers", "Ramapo Mountain State Forest", "About 20 miles from Midtown Manhattan"],
        neighbors=["wayne", "wanaque", "bloomingdale", "ringwood"],
        faqs=[
            ("Is the drive from Pompton Lakes easy?", "Yes — take Route 23 South or I-287 South toward Wayne, then US-46 East into Totowa."),
            ("Do you offer personal branding headshots?", "Yes. They are ideal for coaches, consultants, realtors, speakers and creators."),
        ]),
    "wanaque": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Wanaque, NJ, including Haskell. Corporate, personal branding and residency photos at our Totowa studio, retouched within 24 hours.",
        lead="Headshots for Wanaque and Haskell — corporate, personal branding and residency photos at our Totowa studio.",
        intro=[
            "Wanaque, which includes the Haskell section, is a borough in northern Passaic County best known for the Wanaque Reservoir, one of New Jersey's largest water supplies. I-287 runs through town, making it easy for residents to commute to offices across North Jersey.",
            "Whether you need a fresh LinkedIn photo, a headshot for a new role, or ERAS-ready photos for a medical residency application, our Totowa studio is a straightforward drive from Wanaque — and your retouched photos arrive within 24 hours.",
        ],
        route="From Wanaque, take I-287 South to Route 23 South toward Wayne, then US-46 East into Totowa — our studio is on Route 46.",
        highlights=["Wanaque Reservoir", "Haskell section", "I-287 access"],
        neighbors=["ringwood", "pompton-lakes", "bloomingdale", "wayne"],
        faqs=[
            ("Do you serve Haskell as well as Wanaque?", "Yes — clients from every part of Wanaque, including Haskell, book sessions at our Totowa studio."),
            ("How quickly will I receive my headshots?", "All photos are retouched and delivered within 24 hours."),
        ]),
    "ringwood": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Ringwood, NJ professionals and creators. Corporate and personal branding photos at our Totowa studio, retouched and delivered in 24 hours.",
        lead="Professional and personal branding headshots for Ringwood — worth the scenic drive down to our Totowa studio.",
        intro=[
            "Ringwood is a scenic borough in the northern Highlands, home to Ringwood State Park, Ringwood Manor and the New Jersey State Botanical Garden at Skylands. Many residents work remotely or run their own businesses, so a great headshot does a lot of work on LinkedIn, websites and video calls.",
            "Ringwood clients often book longer sessions to make the most of the trip — capturing corporate headshots and personal branding looks in one visit. Every photo is retouched and delivered within 24 hours.",
        ],
        route="From Ringwood, head south to I-287 South, then Route 23 South toward Wayne and US-46 East into Totowa — our studio is on Route 46.",
        highlights=["Ringwood State Park", "Ringwood Manor", "NJ State Botanical Garden at Skylands"],
        neighbors=["wanaque", "bloomingdale", "pompton-lakes"],
        faqs=[
            ("Is it worth booking a longer session if I'm coming from Ringwood?", "Many clients do — a 30- or 60-minute session gives you time for several outfits and backgrounds in one trip."),
            ("Do you do headshots for remote workers?", "Yes. A professional headshot makes a big difference on LinkedIn, company directories and video-call profiles."),
        ]),
    "bloomingdale": dict(
        kind="borough", county="Passaic County",
        desc="Headshots for Bloomingdale, NJ professionals and creators. Corporate, branding and residency photos at our Totowa studio, retouched in 24 hours.",
        lead="Corporate, personal branding and residency headshots for Bloomingdale — an easy drive down Route 23 to our Totowa studio.",
        intro=[
            "Bloomingdale is a Highlands borough of lake communities — Glen Wild Lake, Lake Iosco and Kampfe Lake among them — with deep Revolutionary War roots: Federal Hill was the site of the 1781 Pompton Mutiny. Residents commute via Route 23 and I-287 to jobs across North Jersey and New York.",
            "We create headshots that help Bloomingdale professionals stand out — clean corporate portraits for LinkedIn and company sites, personal branding photos for entrepreneurs and creators, and ERAS-ready photos for medical residency applicants.",
        ],
        route="From Bloomingdale, take Route 23 South toward Wayne, then US-46 East into Totowa — our studio is on Route 46.",
        highlights=["Lake communities: Glen Wild, Iosco & Kampfe", "Federal Hill (1781 Pompton Mutiny)", "Route 23 & I-287"],
        neighbors=["pompton-lakes", "wanaque", "ringwood", "wayne"],
        faqs=[
            ("How do I get to the studio from Bloomingdale?", "Take Route 23 South toward Wayne, then US-46 East into Totowa. Our studio is at 195 US-46, Suite 9."),
            ("What packages are available?", "1 headshot for $50, 3 for $100, 5 for $150 or 10 for $250 — every package includes professional retouching."),
        ]),
    "milford": dict(
        kind="borough", county="Hunterdon County",
        desc="Headshots for Milford, NJ professionals. Corporate, personal branding and residency photos at our Totowa studio, retouched and delivered within 24 hours.",
        lead="Corporate, personal branding and residency headshots for Milford — book a session at our Totowa studio and get retouched photos within 24 hours.",
        intro=[
            "Milford is a historic river town on the Delaware River in western Hunterdon County, connected to Upper Black Eddy, Pennsylvania by a free bridge. Its small businesses, artists and professionals rely on a strong online presence to reach clients across New Jersey and Pennsylvania.",
            "Our Totowa studio is a drive from Milford, so clients often book a longer session to make the most of the trip — capturing professional headshots and personal branding looks in one visit, with every photo retouched and delivered within 24 hours.",
        ],
        route="From Milford, take I-78 East to I-287 North, then I-80 East toward Totowa — our studio is on US-46.",
        highlights=["Delaware River town", "Milford Historic District", "Bridge to Upper Black Eddy, PA"],
        neighbors=["totowa", "wayne"],
        faqs=[
            ("Is it worth the drive from Milford?", "Many clients from farther away book a 30- or 60-minute session so they leave with several looks from one trip."),
            ("When will I receive my photos?", "All photos are retouched and delivered within 24 hours of your session."),
        ]),
}
