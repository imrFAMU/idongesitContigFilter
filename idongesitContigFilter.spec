/*
A KBase module: idongesitContigFilter
This sample module contains one small method that filters contigs.
*/

module idongesitContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_idongesitContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    /*
        New app which filters contigs in an assemble using both minimum and a maximum length 
    */
    funcdef run_idongesitContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
