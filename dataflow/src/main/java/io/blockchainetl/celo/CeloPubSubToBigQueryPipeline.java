package io.blockchainetl.celo;

import com.google.api.services.bigquery.model.TableRow;
import io.blockchainetl.common.PubSubToBigQueryPipelineOptions;
import io.blockchainetl.common.domain.ChainConfig;
import io.blockchainetl.celo.fns.ConvertBlocksToTableRowsFn;
import io.blockchainetl.celo.fns.ConvertContractsToTableRowsFn;
import io.blockchainetl.celo.fns.ConvertLogsToTableRowsFn;
import io.blockchainetl.celo.fns.ConvertTokenTransfersToTableRowsFn;
import io.blockchainetl.celo.fns.ConvertTokensToTableRowsFn;
import io.blockchainetl.celo.fns.ConvertTracesToTableRowsFn;
import io.blockchainetl.celo.fns.ConvertTransactionsToTableRowsFn;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.DoFn;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static io.blockchainetl.common.PubSubToBigQueryPipeline.readChainConfigs;
import static io.blockchainetl.common.PubSubToBigQueryPipeline.runPipeline;


public class CeloPubSubToBigQueryPipeline {

    public static void main(String[] args) throws IOException, InterruptedException {
        PubSubToBigQueryPipelineOptions options =
            PipelineOptionsFactory.fromArgs(args).withValidation().as(PubSubToBigQueryPipelineOptions.class);

        runCeloPipeline(options);
    }

    static void runCeloPipeline(PubSubToBigQueryPipelineOptions options) {
        List<ChainConfig> chainConfigs = readChainConfigs(options.getChainConfigFile());

        Map<String, Class<? extends DoFn<String, TableRow>>> entityConfigs = new HashMap<>();
        entityConfigs.put("blocks", ConvertBlocksToTableRowsFn.class);
        entityConfigs.put("transactions", ConvertTransactionsToTableRowsFn.class);
        entityConfigs.put("logs", ConvertLogsToTableRowsFn.class);
        entityConfigs.put("token_transfers", ConvertTokenTransfersToTableRowsFn.class);
        entityConfigs.put("traces", ConvertTracesToTableRowsFn.class);
        entityConfigs.put("contracts", ConvertContractsToTableRowsFn.class);
        entityConfigs.put("tokens", ConvertTokensToTableRowsFn.class);
        runPipeline(options,chainConfigs, entityConfigs);
    }
}
