KEYS = (
    '#',
    'G-', 'B-', 'D-', 'Z-', 'I-', 'U-', 'A-', 'E-', 'N-', 'W-', 'Ƨ-', 'Ч-',
    '-G', '-B', '-D', '-Z', '-I', '-U', '-A', '-E', '-N', '-W', '-Ƨ', '-Ч',
)

IMPLICIT_HYPHEN_KEYS = ('Ƨ-','Ч-','-Ƨ','-Ч')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "Ƨ-"

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        '#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'x'),

        'N-': 'q',
        'W-': 'a',
        'A-': 'w',
        'E-': 's',
        'I-': 'e',
        'U-': 'd',
        'D-': 'r',
        'Z-': 'f',
        'B-': 'g',
        'G-': 't',
        'Ƨ-': 'c',
        'Ч-': 'v',

        '-G': 'y',
        '-B': 'h',
        '-D': 'u',
        '-Z': 'j',
        '-I': 'i',
        '-U': 'k',
        '-A': 'o',
        '-E': 'l',
        '-N': 'p',
        '-W': ';',
        '-Ƨ': 'n',
        '-Ч': 'm',

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C', '-D', '-Z'),

        'N-': 'S1',
        'W-': 'S2',
        'A-': 'T-',
        'E-': 'K-',
        'I-': 'P-',
        'U-': 'W-',
        'D-': 'H-',
        'Z-': 'R-',
        'B-': '*3',
        'G-': '*1',
        'Ƨ-': 'A',
        'Ч-': 'O',

        '-G': '*2',
        '-B': '*4',
        '-D': '-F',
        '-Z': '-R',
        '-I': '-P',
        '-U': '-B',
        '-A': '-L',
        '-E': '-G',
        '-N': '-T',
        '-W': '-S',
        '-Ƨ': 'E',
        '-Ч': 'U',

        'no-op': ('res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = 'asset:plover_wagtail:dictionaries'
DEFAULT_DICTIONARIES = (
	'wagtail-tonal-briefs',
	'wagtail-tonal-1char.json',
	'wagtail-tonal-2char.json',
	'wagtail-tonal-commands.json',
	'wagtail-tonal-phrasing.py'
	)
