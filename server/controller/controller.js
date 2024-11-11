const axios = require('axios');
const text=require("../demotext")

// get_Scrapping
function create_scrapping(req,res){
  try {
    if (!req.body) return res.status(400).json("Post HTTP Data not Provided");
    const { websiteLink } = req.body;
    const options = {
      method: 'POST',
      url: 'https://web2meaning.p.rapidapi.com/parse/v2',
      headers: {
        'content-type': 'application/json',
        'X-RapidAPI-Key': process.env.XRAPIDKEY,
        'X-RapidAPI-Host': 'web2meaning.p.rapidapi.com'
      },
      data: {
        url: websiteLink,
        params: {
          domain: true,
          html: false,
          links: false,
          media: {
            audios: false,
            images: true,
            videos: true
          },
          metadata: {
            author: true,
            contentType: true,
            date: {
              publishedTime: true,
              updateTime: true
            },
            description: true,
            favicon: true,
            keywords: true,
            title: true
          },
          nlp: {
            customCategories: [
              'business',
              'entertainment',
              'other',
              'politics',
              'sci.chemistry',
              'sci.computer_science',
              'sci.economics',
              'sci.engineering',
              'sci.geo_science',
              'sci.life_sciences',
              'sci.mathematics',
              'sci.physics',
              'sci.social_science',
              'sports',
              'technology'
            ],
            entities: true,
            isArticle: true,
            isCorporative: false,
            websiteTopic: false
          },
          request: {jsRendering: false},
          text: {
            body: true,
            cleanBody: false,
            fullText: true,
            includeLinks: false,
            lang: true
          }
        }
      }
  };
  async function fetchData() {
      try {
        const response = await axios.request(options);
        console.log(response?.data)
        return res.json(response?.data)
      } catch (error) {
        console.error(error);
      }
    }
  fetchData()  

  } catch (err) {
    return res.status(400).json({ message:` Error while catching ${err.message} `});
  }
    

    
}

// get_Summary
function create_summary(req,res){
    const encodedParams = new URLSearchParams();
    // Text from create scrapping
    const { scrapping } = req.body;
encodedParams.set('text', scrapping);
encodedParams.set('percentage', '30');
    const options = {
      method: 'POST',
      url: 'https://text-summarize-pro.p.rapidapi.com/summarizeFromText',
      headers: {
        'content-type': 'application/x-www-form-urlencoded',
        'X-RapidAPI-Key': '4e1c67e8ffmsh81799791e35ab4cp1a6eb0jsn6a039d266265',
        'X-RapidAPI-Host': 'text-summarize-pro.p.rapidapi.com'
      },
      data: encodedParams,
    };
    async function fetchData() {
        try {
          const response = await axios.request(options);
          console.log(response?.data)
          res.json(response?.data)
        } catch (error) {
          console.error(error);
        }
      }
    fetchData()  
    
}


// get_sentiment
function create_sentiment(req,res){
  const { summary } = req.body;
    const options = {
        method: 'POST',
        url: 'https://microsoft-text-analytics1.p.rapidapi.com/sentiment',
        headers: {
          'content-type': 'application/json',
          'X-RapidAPI-Key': process.env.XRAPIDKEY,
          'X-RapidAPI-Host': 'microsoft-text-analytics1.p.rapidapi.com'
        },
        data: {
          documents: [
            {
              id: '1',
              language: 'en',
              text: summary
            }
          ]
        }
      };

    async function fetchData() {
        try {
          const response = await axios.request(options);
          console.log(response?.data)
          res.json(response?.data)
        } catch (error) {
          console.error(error);
        }
      }
    fetchData()  
    
}


// get_Competitors
function create_competitors(req,res){
  const { business,place } = req.body;
  const options = {
    method: 'POST',
    url: 'https://local-business-data.p.rapidapi.com/search',
    headers: {
      'content-type': 'application/json',
      'X-RapidAPI-Key': '4e1c67e8ffmsh81799791e35ab4cp1a6eb0jsn6a039d266265',
      'X-RapidAPI-Host': 'local-business-data.p.rapidapi.com'
    },
    data: {
      queries: [
        `${business} in ${place}`
      ],
      limit: 10,
      region: 'us',
      language: 'en',
      coordinates: '38.447030, -101.547385',
      zoom: 13,
      dedup: true
    }
  };
    async function fetchData() {
        try {
          const response = await axios.request(options);
        //   this is working
          console.log(response?.data)
          res.json(response?.data);
        } catch (error) {
          console.error(error);
        }
      }
    fetchData()   
}


// get_Entities
function create_entities(req,res){
    const options = {
        method: 'POST',
        url: 'https://microsoft-text-analytics1.p.rapidapi.com/entities/recognition/general',
        headers: {
          'content-type': 'application/json',
          'X-RapidAPI-Key': process.env.XRAPIDKEY,
          'X-RapidAPI-Host': 'microsoft-text-analytics1.p.rapidapi.com'
        },
        data: {
          documents: [
            {
              id: '1',
              language: 'en',
              text: text.summary.slice(5119)
            }
          ]
        }
      };
    async function fetchData() {
        try {
          const response = await axios.request(options);
        //   this is working
          console.log(response?.data.documents[0].entities.forEach((item)=>{
            item
          }))
        //   res.json(response?.data.documents[0].entities.forEach(entity => {
        //     const text = entity?.text;
        //     console.log(text);
        //   }));
        } catch (error) {
          console.error(error);
        }
      }
    fetchData()  
    
}




module.exports={
    create_scrapping,
    create_summary,
    create_entities,
    create_sentiment,
    create_competitors

}