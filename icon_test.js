const ICONS = {
  'gold': '💰', 'stamina': '💖', 'medal': '🏅', 'lumber': '🪵', 'water': '💧',
  'backpack': '🎒', 'chicken feed': '🌽', 'animal feed': '🌾',
  'turnip': '🧅', 'potato': '🥔', 'cucumber': '🥒', 'strawberry': '🍓',
  'cabbage': '🥬', 'tomato': '🍅', 'corn': '🌽', 'onion': '🧅',
  'pumpkin': '🎃', 'pineapple': '🍍', 'eggplant': '🍆', 'carrot': '🥕',
  'sweet potato': '🍠', 'spinach': '🥬', 'green pepper': '🫑',
  'apple': '🍎', 'honey': '🍯', 'bamboo': '🎋', 'mushroom': '🍄',
  'truffle': '🍄', 'grape': '🍇', 'fish': '🐟', 'egg': '🥚',
  'mayonnaise': '🥚', 'milk': '🥛', 'cheese': '🧀', 'wool': '🐑',
  'yarn': '🧶', 'ore': '🪨', 'stone': '🪨', 'branch': '🪵', 'weed': '🌱',
  'flower': '🌷', 'grass': '🌿', 'bracelet': '💍', 'necklace': '📿',
  'earrings': '💎', 'brooch': '🎀', 'gem': '💎', 'recipe': '📜',
  'book': '📖', 'tool': '🔨', 'sickle': '🪝', 'hoe': '⛏️', 'ax': '🪓',
  'hammer': '🔨', 'watering can': '💧', 'fishing rod': '🎣',
  'bell': '🔔', 'brush': '🪥', 'milker': '🥛', 'shears': '✂️',
  'medicine': '💊', 'potion': '🧪', 'wine': '🍷', 'chocolate': '🍫',
  'cake': '🍰', 'cookie': '🍪', 'ice cream': '🍦', 'bread': '🍞',
  'pizza': '🍕', 'sushi': '🍣', 'noodle': '🍜', 'rice': '🍚',
  'dog': '🐶', 'horse': '🐴', 'chicken': '🐔', 'cow': '🐄', 'sheep': '🐑',
  'weather': '🌤️', 'season': '🌸', 'day': '📅', 'year': '🗓️'
};

function getIcon(name) {
  const n = name.toLowerCase();
  for (const [key, icon] of Object.entries(ICONS)) {
    if (n.includes(key)) return icon;
  }
  // Fallbacks based on category/type
  if (n.includes('level') || n.includes('max') || n.includes('infinite')) return '⭐';
  return '📦'; // Default box
}

console.log(getIcon('Max Lumber'));
console.log(getIcon('Cabbage Seed'));
console.log(getIcon('Turnip'));
