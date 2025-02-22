SKILLS_CHOICES = [
    # Основні мови програмування
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('Java', 'Java'),
    ('C', 'C'),
    ('C++', 'C++'),
    ('C#', 'C#'),
    ('Go', 'Go'),
    ('Rust', 'Rust'),
    ('Swift', 'Swift'),
    ('Kotlin', 'Kotlin'),
    ('Dart', 'Dart'),
    ('Objective-C', 'Objective-C'),
    ('TypeScript', 'TypeScript'),
    ('PHP', 'PHP'),
    ('Ruby', 'Ruby'),
    ('Perl', 'Perl'),
    ('Scala', 'Scala'),
    ('Haskell', 'Haskell'),
    ('Elixir', 'Elixir'),
    ('Erlang', 'Erlang'),
    ('Lua', 'Lua'),
    ('F#', 'F#'),
    ('Bash', 'Bash'),
    ('PowerShell', 'PowerShell'),
    ('Shell Scripting', 'Shell Scripting'),
    ('R', 'R'),
    ('MATLAB', 'MATLAB'),
    ('Julia', 'Julia'),
    ('COBOL', 'COBOL'),
    ('Fortran', 'Fortran'),
    ('Lisp', 'Lisp'),
    ('Prolog', 'Prolog'),
    ('Groovy', 'Groovy'),
    ('VB.NET', 'VB.NET'),
    ('Assembly', 'Assembly'),

    # Веб-розробка (Frontend)
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('SASS/SCSS', 'SASS/SCSS'),
    ('Tailwind CSS', 'Tailwind CSS'),
    ('Bootstrap', 'Bootstrap'),
    ('React', 'React'),
    ('Next.js', 'Next.js'),
    ('Vue.js', 'Vue.js'),
    ('Nuxt.js', 'Nuxt.js'),
    ('Angular', 'Angular'),
    ('Svelte', 'Svelte'),
    ('Ember.js', 'Ember.js'),
    ('jQuery', 'jQuery'),
    ('Three.js', 'Three.js'),
    ('Gatsby', 'Gatsby'),
    ('Grunt', 'Grunt'),
    ('Parcel', 'Parcel'),
    ('Pug', 'Pug'),

    # Веб-розробка (Backend)
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('FastAPI', 'FastAPI'),
    ('Express.js', 'Express.js'),
    ('NestJS', 'NestJS'),
    ('Spring Boot', 'Spring Boot'),
    ('ASP.NET Core', 'ASP.NET Core'),
    ('Ruby on Rails', 'Ruby on Rails'),
    ('Laravel', 'Laravel'),
    ('Symfony', 'Symfony'),
    ('CodeIgniter', 'CodeIgniter'),
    ('Phoenix', 'Phoenix'),
    ('Golang Gin', 'Golang Gin'),
    ('Fiber', 'Fiber'),
    ('Elixir Phoenix', 'Elixir Phoenix'),
    ('Sails.js', 'Sails.js'),
    ('Koa.js', 'Koa.js'),

    # Бази даних
    ('SQL', 'SQL'),
    ('NoSQL', 'NoSQL'),
    ('MySQL', 'MySQL'),
    ('PostgreSQL', 'PostgreSQL'),
    ('SQLite', 'SQLite'),
    ('MongoDB', 'MongoDB'),
    ('Cassandra', 'Cassandra'),
    ('Redis', 'Redis'),
    ('Firebase', 'Firebase'),
    ('DynamoDB', 'DynamoDB'),
    ('GraphQL', 'GraphQL'),
    ('Supabase', 'Supabase'),
    ('ElasticSearch', 'ElasticSearch'),
    ('CouchDB', 'CouchDB'),
    ('Neo4j', 'Neo4j'),
    ('Apache HBase', 'Apache HBase'),
    ('Amazon Redshift', 'Amazon Redshift'),

    # DevOps та хмарні технології
    ('Docker', 'Docker'),
    ('Kubernetes', 'Kubernetes'),
    ('Terraform', 'Terraform'),
    ('Ansible', 'Ansible'),
    ('CI/CD', 'CI/CD'),
    ('GitHub Actions', 'GitHub Actions'),
    ('Jenkins', 'Jenkins'),
    ('AWS', 'AWS'),
    ('Azure', 'Azure'),
    ('Google Cloud', 'Google Cloud'),
    ('IBM Cloud', 'IBM Cloud'),
    ('OpenShift', 'OpenShift'),
    ('Pulumi', 'Pulumi'),
    ('CloudFormation', 'CloudFormation'),
    ('Vagrant', 'Vagrant'),

    # Data Science / Machine Learning
    ('Machine Learning', 'Machine Learning'),
    ('Deep Learning', 'Deep Learning'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Data Science', 'Data Science'),
    ('Big Data', 'Big Data'),
    ('Pandas', 'Pandas'),
    ('NumPy', 'NumPy'),
    ('SciPy', 'SciPy'),
    ('Matplotlib', 'Matplotlib'),
    ('Seaborn', 'Seaborn'),
    ('TensorFlow', 'TensorFlow'),
    ('PyTorch', 'PyTorch'),
    ('Keras', 'Keras'),
    ('OpenCV', 'OpenCV'),
    ('Scikit-learn', 'Scikit-learn'),
    ('XGBoost', 'XGBoost'),
    ('LightGBM', 'LightGBM'),
    ('NLTK', 'NLTK'),
    ('spaCy', 'spaCy'),
    ('Hugging Face', 'Hugging Face'),

    # Кібербезпека
    ('Cybersecurity', 'Cybersecurity'),
    ('Penetration Testing', 'Penetration Testing'),
    ('Ethical Hacking', 'Ethical Hacking'),
    ('Cryptography', 'Cryptography'),
    ('SIEM', 'SIEM'),
    ('SOC', 'SOC'),
    ('Network Security', 'Network Security'),
    ('Forensics', 'Forensics'),
    ('Firewalls', 'Firewalls'),
    ('IDS/IPS', 'IDS/IPS'),
    ('DDoS Protection', 'DDoS Protection'),
    ('Reverse Engineering', 'Reverse Engineering'),

    # Геймдев
    ('Game Development', 'Game Development'),
    ('Unity', 'Unity'),
    ('Unreal Engine', 'Unreal Engine'),
    ('Godot', 'Godot'),
    ('Cocos2d', 'Cocos2d'),
    ('AR/VR', 'AR/VR'),
    ('Blender', 'Blender'),
    ('Game Design', 'Game Design'),
    ('C# (Unity)', 'C# (Unity)'),
    ('Java (Android Games)', 'Java (Android Games)'),

    # UI/UX дизайн
    ('UI/UX Design', 'UI/UX Design'),
    ('Figma', 'Figma'),
    ('Adobe XD', 'Adobe XD'),
    ('Sketch', 'Sketch'),
    ('InVision', 'InVision'),
    ('Balsamiq', 'Balsamiq'),
    ('Wireframing', 'Wireframing'),
    ('Prototyping', 'Prototyping'),
    ('User Research', 'User Research'),

    # Інше
    ('Blockchain', 'Blockchain'),
    ('Smart Contracts', 'Smart Contracts'),
    ('IoT', 'IoT'),
    ('Embedded Systems', 'Embedded Systems'),
    ('Networking', 'Networking'),
    ('Robotics', 'Robotics'),
    ('Quantum Computing', 'Quantum Computing'),
    ('AR/VR Development', 'AR/VR Development'),
    ('5G', '5G'),
    ('Edge Computing', 'Edge Computing'),
    ('Serverless Computing', 'Serverless Computing'),
]

JOB_FORMAT_CHOICES = [
    ('Full-time', 'Full-time'),
    ('Part-time', 'Part-time'),
    ('Freelance', 'Freelance'),
    ('Remote', 'Remote'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
]


