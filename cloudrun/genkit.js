import { genkit, z } from 'genkit';
import { vertexAI } from '@genkit-ai/google-genai';

const projectId = process.env.FIREBASE_PROJECT_ID || 'playground-0505';
const location = process.env.VERTEX_LOCATION || 'asia-south1';
const ai = genkit({ plugins: [vertexAI({ projectId, location })] });
const model = vertexAI.model('gemini-2.0-flash-001');

const verificationSchema = z.object({
  genuine: z.boolean(), confidence: z.number(), reason: z.string(), category: z.string(),
  priority: z.number(), duplicateSignals: z.array(z.string()).default([]), needsHumanReview: z.boolean()
});

export const verifyReportFlow = ai.defineFlow(
  { name: 'verifyReport', inputSchema: z.object({ description: z.string(), location: z.string(), state: z.string() }), outputSchema: verificationSchema },
  async (input) => {
    const { output } = await ai.generate({
      model,
      prompt: `You are JanSetu's civic integrity agent for India. Review this report and return JSON only. A genuine report describes a specific plausible public issue, a place, and observable impact. Do not reject multilingual or informal writing. Flag low confidence or suspected manipulation for human review. Report: ${JSON.stringify({ ...input, description: input.description.slice(0, 1600) })}`,
      output: { schema: verificationSchema },
      config: { temperature: 0.1, maxOutputTokens: 220 }
    });
    return output;
  }
);

export const areaPolicyFlow = ai.defineFlow(
  { name: 'areaPolicy', inputSchema: z.object({ area: z.string(), reports: z.array(z.any()) }), outputSchema: z.object({ headline: z.string(), topCategory: z.string(), summary: z.string(), recommendedAction: z.string(), confidence: z.number() }) },
  async (input) => {
    const { output } = await ai.generate({
      model,
      prompt: `You are JanSetu's area intelligence agent. Analyse these citizen reports for ${input.area}. Return JSON only. Do not invent counts, places, or commitments. Reports: ${JSON.stringify(input.reports.slice(0, 25))}`,
      output: { schema: z.object({ headline: z.string(), topCategory: z.string(), summary: z.string(), recommendedAction: z.string(), confidence: z.number() }) },
      config: { temperature: 0.1, maxOutputTokens: 220 }
    });
    return output;
  }
);
