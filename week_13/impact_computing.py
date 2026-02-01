"""
Week 13: Impact of Computing - Practice Questions
=================================================
Big Idea: IOC (Impact of Computing)

Review and discussion questions for the AP CSP exam.
"""

# =============================================================================
# Study Guide: Key Terms
# =============================================================================

KEY_TERMS = {
    "Digital Divide": """
        The gap between those with and without access to computing technology.
        Factors: geography, economics, age, infrastructure.
    """,

    "PII": """
        Personally Identifiable Information - data that can identify an individual.
        Examples: name, SSN, address, biometrics, IP address.
    """,

    "Encryption": """
        Process of encoding data so only authorized parties can read it.
        HTTPS uses encryption to secure web traffic.
    """,

    "Phishing": """
        Fraudulent attempt to obtain sensitive information by pretending
        to be a trustworthy source (fake emails, websites).
    """,

    "Open Source": """
        Software whose source code is publicly available for anyone to
        view, modify, and distribute.
    """,

    "Copyright": """
        Legal right that protects original works of authorship.
        Automatic upon creation; no registration required.
    """,

    "Creative Commons": """
        Licensing system that allows creators to specify how their
        work can be shared and used by others.
    """,

    "Crowdsourcing": """
        Obtaining services, ideas, or content from a large group of people,
        typically via the internet.
    """,

    "Algorithm Bias": """
        When an algorithm produces unfair outcomes due to biased data
        or design choices. Can discriminate against groups.
    """,

    "Citizen Science": """
        Scientific research conducted with participation from
        the general public, often through computing platforms.
    """
}


# =============================================================================
# Practice: Analyzing Computing Innovations
# =============================================================================

def analyze_innovation(name, description):
    """
    Framework for analyzing a computing innovation.

    For each innovation, consider:
    1. What problem does it solve?
    2. What data does it use/collect?
    3. What are the benefits?
    4. What are potential harms?
    5. Who might be affected differently?
    """
    print(f"\n{'='*50}")
    print(f"ANALYZING: {name}")
    print(f"{'='*50}")
    print(f"\nDescription: {description}")
    print("\nConsider:")
    print("  1. Purpose: What problem does this solve?")
    print("  2. Data: What information does it collect/use?")
    print("  3. Benefits: Who benefits and how?")
    print("  4. Harms: What are potential negative effects?")
    print("  5. Equity: Does it affect all users equally?")


# Sample innovations to analyze
INNOVATIONS = [
    ("Facial Recognition", "AI system that identifies individuals from images/video"),
    ("Social Media Algorithms", "Systems that decide what content users see in their feeds"),
    ("GPS Navigation", "Satellite-based system for determining location and directions"),
    ("Online Learning Platforms", "Websites and apps for educational content and classes"),
    ("Fitness Trackers", "Wearable devices that monitor health metrics"),
    ("Recommendation Systems", "Algorithms that suggest products, videos, or content"),
]


# =============================================================================
# Practice: Privacy Scenarios
# =============================================================================

PRIVACY_SCENARIOS = [
    {
        "scenario": "A weather app asks for your location to provide local forecasts.",
        "question": "Is sharing your location justified?",
        "considerations": [
            "Location data reveals where you live and travel",
            "The app needs location to function properly",
            "Could the data be shared with third parties?",
            "Is approximate location sufficient?"
        ]
    },
    {
        "scenario": "A social media site stores everything you've ever posted.",
        "question": "What are the privacy implications?",
        "considerations": [
            "Old posts may no longer represent your views",
            "Data could be accessed in a breach",
            "Information could affect job prospects",
            "You should have the right to delete data"
        ]
    },
    {
        "scenario": "A store tracks your purchases to offer personalized coupons.",
        "question": "Is this beneficial or concerning?",
        "considerations": [
            "Personalization can be convenient",
            "Detailed purchase history reveals a lot about you",
            "Data could be sold to other companies",
            "Opting out may mean missing discounts"
        ]
    }
]


# =============================================================================
# Practice: Bias in Algorithms
# =============================================================================

BIAS_EXAMPLES = [
    {
        "system": "Hiring Algorithm",
        "bias": "Trained on past hiring data where most employees were male",
        "effect": "Unfairly ranks female candidates lower",
        "solution": "Audit training data, test for disparate impact"
    },
    {
        "system": "Facial Recognition",
        "bias": "Training data had mostly lighter skin tones",
        "effect": "Lower accuracy for darker skin tones",
        "solution": "Diverse training data, independent testing"
    },
    {
        "system": "Credit Scoring",
        "bias": "Uses zip code as a factor",
        "effect": "Discriminates against certain neighborhoods",
        "solution": "Remove proxies for protected characteristics"
    },
    {
        "system": "Search Engine",
        "bias": "Reflects historical search patterns",
        "effect": "May reinforce stereotypes in results",
        "solution": "Algorithmic fairness reviews, diverse teams"
    }
]


# =============================================================================
# Interactive Review
# =============================================================================

def review_key_terms():
    """Flashcard-style review of key terms."""
    import random

    terms = list(KEY_TERMS.keys())
    random.shuffle(terms)

    print("\n" + "="*50)
    print("KEY TERMS REVIEW")
    print("="*50)

    for term in terms:
        input(f"\nDefine: {term} (press Enter to see definition)")
        print(f"  {KEY_TERMS[term].strip()}")


def discuss_innovation():
    """Guided discussion of a random innovation."""
    import random

    name, desc = random.choice(INNOVATIONS)
    analyze_innovation(name, desc)

    print("\nWrite your analysis for each point!")


if __name__ == "__main__":
    print("="*50)
    print("Week 13: Impact of Computing Review")
    print("="*50)

    print("\nThis module contains study materials for IOC topics.")
    print("\nAvailable functions:")
    print("  review_key_terms() - Flashcard review of terms")
    print("  discuss_innovation() - Analyze a random innovation")

    # Uncomment to use:
    # review_key_terms()
    # discuss_innovation()
